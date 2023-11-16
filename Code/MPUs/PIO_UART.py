# based on #https://github.com/micropython/micropython/tree/master/examples/rp2
# ran out of real UARTs so this will have to do
# gc.collect() MUST be in the main loop, otherwise it will stuff up interrupts
# and run in cbRxSM4() once it uses extra heap    ahghhhh!!
#
# Anyway, yet again still not reliable in a production environment with other 
# things running and interrupting.  Send is reliable, but NOT receive

from machine import Pin, UART
from rp2 import PIO, StateMachine, asm_pio
import array

UART_Baud = 9600
PIO_UART0_TX_pin = 8
PIO_UART0_RX_pin = 9

################################################################################
# UART PIO TX

@asm_pio(sideset_init=PIO.OUT_HIGH, out_init=PIO.OUT_HIGH, out_shiftdir=PIO.SHIFT_RIGHT)
def uart_tx():
    pull()                          # Block with TX deasserted until data available   
    set(x, 7)  .side(0)       [7]   # Initialise bit counter, assert start bit for 8 cycles
    label("bitloop")                # Shift out 8 data bits, 8 execution cycles per bit
    out(pins, 1)              [6]
    jmp(x_dec, "bitloop")
    nop()      .side(1)       [6]   # Assert stop bit for 8 cycles total (incl 1 for pull())

TxSM0 = StateMachine(0, uart_tx, freq=8 * UART_Baud, 
    sideset_base=Pin(PIO_UART0_TX_pin), out_base=Pin(PIO_UART0_TX_pin))
TxSM0.active(True)

def WriteLine(s):
    for c in s:
        TxSM0.put(ord(c))
        

################################################################################
# UART PIO RX, use interrupts per character received to recreate 
# sentence, and when complete set glogal LineReady to True


@asm_pio(in_shiftdir=PIO.SHIFT_RIGHT)
def uart_rx():
    label("start")
    wait(0, pin, 0)                 # Stall until start bit is asserted
    set(x, 7)               [10]    # Preload counter,delay 12 cycle (mid first bit)
    label("bitloop")
    in_(pins, 1)                    # Shift data bit into ISR  
    jmp(x_dec, "bitloop")   [6]     # Loop 8 times, each loop iteration is 8 cycles
    jmp(pin, "good_stop")           # Check stop bit (should be high)
    wait(1, pin, 0)                 # framing err/brk - wait for line to return to idle state
    jmp("start")                    # ..so skip data push
    label("good_stop")              # No delay before returning in case the TX clock too fast
    push(block)                   # 4 word buf
    irq(block, 0)                 # 1 byte ready for assembly by ISR

Index = 0
LineReady = False
NumChars = 0
Line = array.array('b',(0 for _ in range(256)))
                      
def cbRxSM4(cbRxSM4):
    # Assemble lines by interrupting per byte received until '\n'
    global Index, LineReady, Line, NumChars
    print(Index)
    c = RxSM4.get() >> 24  
    Line[Index] = c
    Index += 1        
    if c == ord('\n') or Index == 255:
        NumChars = Index
        Index = 0
        LineReady = True

RxSM4 = StateMachine(4, uart_rx, freq=8 * UART_Baud, in_base=Pin(PIO_UART0_RX_pin), 
                     jmp_pin=Pin(PIO_UART0_RX_pin))
RxSM4.irq(cbRxSM4)
RxSM4.active(True)

def ReadLine():
    global LineReady
    if LineReady:
        LineReady = False
        return bytes(Line[0:NumChars])

