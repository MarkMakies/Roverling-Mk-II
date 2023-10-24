################################################################################
# Roverling Mk II - RCinterface.py RC Interface (mine: Spektrum AR6200 Rx, DX6i Tx)
# Interrupt on both edges to mark tick_us points, process later at a reduced
# rate, as required, to keep these IRQ routines as short as possible

from machine import Pin, Timer
from time import ticks_us
from array import array

# Parameters
RCSamplePeriod = 100    

ch1 = Pin(5,Pin.IN)
ch2 = Pin(4,Pin.IN)
ch3 = Pin(3,Pin.IN)
ch4 = Pin(2,Pin.IN)
ch5 = Pin(1,Pin.IN)
ch6 = Pin(0,Pin.IN)

dataR = array('B',[0]*6)

tt = ticks_us()
CHtimes = array('H',[tt]*12)

def cbIntCh1(ch1):
    global CHtimes
    if ch1.value() == 1:
        CHtimes[0] = ticks_us()
    else:
        CHtimes[1] = ticks_us()

def cbIntCh2(ch2):
    global CHtimes
    if ch2.value() == 1:
        CHtimes[2] = ticks_us()
    else:
        CHtimes[3] = ticks_us()

def cbIntCh3(ch3):
    global CHtimes
    if ch3.value() == 1:
        CHtimes[4] = ticks_us()
    else:
        CHtimes[5] = ticks_us()

def cbIntCh4(ch4):
    global CHtimes
    if ch4.value() == 1:
        CHtimes[6] = ticks_us()
    else:
        CHtimes[7] = ticks_us()

def cbIntCh5(ch5):
    global CHtimes
    if ch5.value() == 1:
        CHtimes[8] = ticks_us()
    else:
        CHtimes[9] = ticks_us()

def cbIntCh6(ch6):
    global CHtimes
    if ch6.value() == 1:
        CHtimes[10] = ticks_us()
    else:
        CHtimes[11] = ticks_us()

ch1.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=cbIntCh1)
ch2.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=cbIntCh2)
ch3.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=cbIntCh3)
ch4.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=cbIntCh4)
ch5.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=cbIntCh5)
ch6.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=cbIntCh6)

RCavg = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

def UpdateRC():
    global dataR
    global RCavg
    
    for i in range(6):
        diff = CHtimes[2*i+1] - CHtimes[2*i]
        if diff < 2500 and  diff > 800:
            NewVal = int(min(max((diff - 1000) / 10, 0), 100))
            RCavg[i].append(NewVal)
            RCavg[i].pop(0)                  # use median of last 5 samples
            tmpList = []
            tmpList.extend(RCavg[i])
            tmpList.sort()
            dataR[i] = tmpList[2]           # centre position implies 2 values above and 2 below

def cbRCSampleTimer(t):
    UpdateRC()
  
rcSampleTimer = Timer(period=RCSamplePeriod , mode=Timer.PERIODIC, callback=cbRCSampleTimer)
