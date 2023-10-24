################################################################################
# Roverling Mk II - Motor Control Processor
print('Roverling Mk II - Motor & RC Control main.py on RP2040')

from machine import Pin, PWM, ADC, UART
from time import sleep_ms
from gc import collect
import neopixel

# my modules
from RCinterface import dataR
from QuadDec import dataV
from Comms import SendTelemetry, RecvCommand, dataCMD

Muart = UART(1, baudrate=1_000_000, tx=Pin(8), rx=Pin(9))

################################################################################
# LED

NeoPin = Pin(16,Pin.OUT)
Neo = neopixel.NeoPixel(NeoPin,1)
LastLEDstate = True
RGBon, RGBoff = (20,0,0), (0,0,0)

Neo[0]=(20, 0, 0)
neopixel.NeoPixel.write(Neo)

def LEDupdate(mode='none'):
    global Neo, LastLEDstate, RGBon, RGBoff

    if mode == 'GreenSolid':
        RGBon, RGBoff = (20,0,0), (20,0,0)
    elif mode == 'RedSolid':
        RGBon, RGBoff = (0,20,0), (0,20,0)
    elif mode == 'YellowFlash':
        RGBon, RGBoff = (6,20,0), (0,0,0)
    elif mode == 'PinkFlash':
        RGBon, RGBoff = (5,50,10), (0,0,0)

    if not LastLEDstate:
        Neo[0] = RGBon
        LastLEDstate = True
    else:
        Neo[0] = RGBoff
        LastLEDstate = False

    neopixel.NeoPixel.write(Neo)

LEDupdate('RedSolid')

################################################################################
# Motor Current
Lsens = ADC(Pin(28))
Rsens = ADC(Pin(29))

def GetMotorI():       
    global LMamps, RMamps
    ICoeff = 20000  # 377uA/A, over 2k2, => 0.894 V/A
    LMamps = Lsens.read_u16() / ICoeff
    RMamps = Rsens.read_u16() / ICoeff

################################################################################
# Motor Control LM18200 H-bridge

PWMfreq = 50000

LeftDIR = Pin(15, Pin.OUT, value = 0)
LeftBRK = Pin(25, Pin.OUT, value = 1)
LeftPWM = PWM(Pin(27))
LeftPWM.freq(PWMfreq)
LeftPWM.duty_u16(0)

RightDIR = Pin(14, Pin.OUT, value = 0)
RightBRK = Pin(24, Pin.OUT, value = 1)
RightPWM = PWM(Pin(26))
RightPWM.freq(PWMfreq)
RightPWM.duty_u16(0)

def MotDrive(left = 'off', right = 'off'):
    global LeftPower, RightPower
    maxPWM = 2**16 - 1
    if left == 'off':           # driver off, no current
        LeftPWM.duty_u16(0)
        LeftBRK.value(1)
        LeftPower = 0
    else:
        LD = int(left)
        if LD == 0:             # active brake: source 1 & source 2
            LeftPWM.duty_u16(maxPWM)
            LeftBRK.value(1)
            LeftDIR.value(0)
            LeftPower = 0
        elif LD > 0:            # going forward:" source 1 & sink 2"
            LeftPWM.duty_u16(LD)
            LeftBRK.value(0)
            LeftDIR.value(1)
            LeftPower = LD
        else:                   # going back:" sink 1 & source 2"
            LeftPWM.duty_u16(0-LD)
            LeftBRK.value(0)
            LeftDIR.value(0)   
            LeftPower = LD         
    
    if right == 'off':  
        RightPWM.duty_u16(0)
        RightBRK.value(1)
        RightPower = 0
    else:
        RD = int(right)
        if RD == 0:  
            RightBrake = True
            RightPWM.duty_u16(maxPWM)
            RightBRK.value(1)
            RightDIR.value(0)
            RightPower = 0
        elif RD > 0:            
            RightPWM.duty_u16(RD)
            RightBRK.value(0)
            RightDIR.value(0)
            RightPower = RD
        else:
            RightPWM.duty_u16(0-RD)
            RightBRK.value(0)
            RightDIR.value(1)  
            RightPower = RD   

MotDrive()

################################################################################
# Steering Servo
# 20ms cycle, pulse 1-2ms, range adj - trial and error to find limits

Scentre = 5300
Slow = 3900         # +/- 30 deg
Shigh = 6200

SteeringServo = PWM(Pin(18))
SteeringServo.freq(50)
SteeringServo.duty_u16(Scentre)

PanServo = PWM(Pin(6))
PanServo.freq(50)

Tlow  = 3300
Tcentre = 4900
Thigh = 8000

TiltServo = PWM(Pin(7))
TiltServo.freq(50)
TiltServo.duty_u16(Tcentre)

################################################################################
# Main Loop

dataM = [0] * 6
LeftPower, RightPower = 0, 0

def GetData():
    global dataM
    dataM[0] = dataV[0]
    dataM[1] = dataV[1]

    GetMotorI()
    dataM[2] = LMamps
    dataM[3] = RMamps
    dataM[4] = LeftPower
    dataM[5] = RightPower

Scheduler = 0
LEDupdate('GreenSolid')
Mode = 'Normal'

while True:
    sleep_ms(1)
    Scheduler += 1

    if (Scheduler - 2) % 50 == 0: 
        # ch1-6 ===  dataR[0]-[5]
        if Mode == 'RC':
            if dataR[0] > 10:                       # as THR off defaults to about 7%               
                dd = int(dataR[0] / 100 * 2**16)    # ch1 thro: PWM
                if dataR[4] < 90:                   # ch5 gear: direction
                    MotDrive(dd,dd)
                else:
                    MotDrive(-dd,-dd)
            else:
                MotDrive(0, 0)
            
            S = (dataR[1]-50) / 50      #ch2 aile: steering
            if S > 0.02:
                y = Scentre + ((Shigh - Scentre) * S) 
            elif S < -0.02:
                y = Scentre + ((Scentre - Slow) * S) 
            else:
                y = Scentre
            SteeringServo.duty_u16(int(y))


            T = (dataR[2]-50) / 50      #ch3 elev: camera tilt
            if T > 0.05:
                y = Tcentre + ((Thigh - Tcentre) * T) 
            elif T < -0.05:
                y = Tcentre + ((Tcentre - Tlow) * T) 
            else:
                y = Tcentre
            TiltServo.duty_u16(int(y))


    if (Scheduler - 10) % 100 == 0:          #100ms 10ms offset
        if RecvCommand(Muart):
            print('New Command: ', dataCMD)

    if (Scheduler - 20) % 200 == 0:    
        GetData()                       
        SendTelemetry(Muart, dataM, dataR)      
        print(dataR, dataM)   

        if dataR[5] > 80:
            if Mode == 'Normal':
                Mode = 'RC'
                LEDupdate('PinkFlash')
        else:
            if Mode == 'RC':
                Mode = 'Normal'
                MotDrive()  
                SteeringServo.duty_u16(Scentre)
                TiltServo.duty_u16(Tcentre)
                LEDupdate('GreenSolid')

        collect()

    if (Scheduler - 33) % 250 == 0:  
        LEDupdate()                         # aka flash if selected

    if (Scheduler - 20) % 1000 == 0:         #1000ms 5ms offset   
        pass
        #collect()
