################################################################################
# Roverling Mk II - Quadrature Decoder
# Count transitions using RP2040 PIO based state machine, no CPU cycles and then
# use timer based interrupt to read accumulated counts, aka velocity. - 5ms
# Motor quadrature optical encoder: 100 CPT, 17.83:1, 1783 counts per revolution

from machine import Pin, Timer
from rp2 import asm_pio, StateMachine
from array import array
import time

REncApin = Pin(12, Pin.IN, Pin.PULL_UP)
REncBpin = Pin(13, Pin.IN, Pin.PULL_UP)  
LEncApin = Pin(10, Pin.IN, Pin.PULL_UP)
LEncBpin = Pin(11, Pin.IN, Pin.PULL_UP)  

# Initis
PrevREnc = 0
PrevLEnc = 0

dataV = array('f', [0]*2)

# Parameters
EncoderSamplePeriod = 50      
Counts2Vel = 400

@asm_pio()
def encoder():       
    # adapted from https://github.com/adamgreen/QuadratureDecoder
    # In C/C++ can define base, which needs to be 0 for jump table to work
    # in python not working, but padding out to exactly 32 instructions fixes it
    # 16 element jump table based on 4-bit encoder last state and current state.

    jmp('delta0')     # 00-00
    jmp('delta0')     # 00-01
    jmp('delta0')     # 00-10
    jmp('delta0')     # 00-11

    jmp('plus1')      # 01-00
    jmp('delta0')     # 01-01
    jmp('delta0')     # 01-10
    jmp('minus1')     # 01-11

    jmp('minus1')     # 10-00
    jmp('delta0')     # 10-01
    jmp('delta0')     # 10-10
    jmp('plus1')      # 10-11

    jmp('delta0')     # 11-00
    jmp('delta0')     # 11-01
    jmp('delta0')     # 11-10
    jmp('delta0')     # 11-11
                        
    label('delta0')     # Program actually starts here.
    mov(isr, null)      # Make sure that the input shift register is cleared when table jumps to delta0.
    in_(y, 2)           # Upper 2-bits of address are formed from previous encoder pin readings Y -> ISR[3,2]
    mov(y, pins)        # Lower 2-bits of address are formed from current encoder pin readings. PINS -> Y
    in_(y, 2)           # Y -> ISR[1,0]
    mov(pc, isr)        # Jump into jump table which will then jump to delta0, minus1, or plus1 labels.

    label('minus1')
    jmp(x_dec,'output') # Decrement x
    jmp('output')

    label('plus1')
    mov(x, invert(x))   # Increment x by calculating x=~(~x - 1)
    jmp(x_dec,'next2')
    label('next2')
    mov(x, invert(x))

    label('output')
    mov(isr, x)         #Push out updated counter.
    push(noblock)
    jmp('delta0')

    nop()                #need to pad out to exactly 32 instructions
    nop()
    nop()

RightMotorEncoder = StateMachine(0, encoder, freq=1000000, in_base=REncApin)
LeftMotorEncoder = StateMachine(1, encoder, freq=1000000, in_base=LEncApin)

def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:          # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)                 # compute negative value
    return val                                  # return positive value as is

def QueryEncoders(): 
    global PrevLEnc, PrevREnc
    global LeftVel, RightVel

    k = 0
    while (LeftMotorEncoder.rx_fifo() > 0) and (k < 4):    # empty FIFO - last value used
        k += 1
        LEE = LeftMotorEncoder.get()
    if k > 0:
        LEE = twos_comp(LEE, 32)
        LE = LEE - PrevLEnc
        PrevLEnc = LEE
    else:
        LE = 0

    k = 0
    while (RightMotorEncoder.rx_fifo() > 0) and (k < 4):  
        k += 1
        REE = RightMotorEncoder.get()
    if k > 0:
        REE = twos_comp(REE, 32)
        RE = REE - PrevREnc
        PrevREnc = REE
    else:
        RE = 0
    
    dataV[0], dataV[1] = LE/ Counts2Vel, RE/Counts2Vel


def cbEncSampleTimer(t):
    QueryEncoders()
    
RightMotorEncoder.active(1)
LeftMotorEncoder.active(1)

EncSampleTimer = Timer(period=EncoderSamplePeriod , mode=Timer.PERIODIC, callback=cbEncSampleTimer)
