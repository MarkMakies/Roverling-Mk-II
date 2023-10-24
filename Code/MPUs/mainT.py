################################################################################
# Roverling Mk II - Telemetry Processor
print('Roverling Mk II - Telemetry Processor main.py on RP2040')

from machine import Pin, I2C, UART, ADC
from time import sleep_ms, sleep_us, ticks_ms, ticks_us
from gc import collect
import neopixel
from cryptolib import aes

# my modules
from GPS import ReadGPS, dataGPS
from IMU import ReadIMU, dataIMU
from Packets import AssemPkt_T, DisAssemPkt_T, AssemPkt_C, DisAssemPkt_C
from Comms import RecvTelemetry, dataMOT, SendCommand

Tuart = UART(1, baudrate=1_000_000, tx=Pin(4), rx=Pin(5))

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
        RGBon, RGBoff = (0,40,0), (0,40,0)
    elif mode == 'YellowFlash':
        RGBon, RGBoff = (6,20,0), (0,0,0)
    elif mode == 'PinkFlash':
        RGBon, RGBoff = (5,50,10), (0,0,0)
    elif mode == 'BlueSolid':
        RGBon, RGBoff = (0,0,30), (0,0,30)
    if not LastLEDstate:
        Neo[0] = RGBon
        LastLEDstate = True
    else:
        Neo[0] = RGBoff
        LastLEDstate = False

    neopixel.NeoPixel.write(Neo)

LEDupdate('RedSolid')

################################################################################
# LoRa

from sx1262 import SX1262
sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=3, irq=6, rst=7, gpio=2)
# Time On Air : Telemetry 64 bits, 195ms, Control 16 bits, 82ms
# At BW=250kHz, SF=9, CR=1/5, Date Rate = 1,758bps
# for max power current limit must be changed for 60 - 140 and LDO enabled
#
sx.begin(freq=920, bw=250.0, sf=9, cr=5, syncWord=0x12,
         power=22, currentLimit=140.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)

NewCmd = False
NewCmdPkt = [0x00] * 16
SNR, RSSI = 0.0, 0.0

def cbLoRa(events):
    global NewCmd
    global NewCmdPkt
    global SNR
    global RSSI
    if events & SX1262.RX_DONE:
        msg, err = sx.recv()
        error = SX1262.STATUS[err]
        if err == 0:
            NewCmd = True
            NewCmdPkt = msg
            SNR = sx.getSNR()
            RSSI = sx.getRSSI()
        else:
            print('LoRa Rx Error: ', error)
    elif events & SX1262.TX_DONE:
        pass                        #TX done    
    else:
        print('LoRa unknown interrupt: ', events)


VBatList = [0] * 9

################################################################################
# Battery Voltage 5cell LiPo system (https://blog.ampow.com/lipo-voltage-chart/)

Vbat = ADC(Pin(29))
def GetVbat():
    global VbatList
    VbatCoeff = 3050                        # through testing
    V = Vbat.read_u16() / VbatCoeff / 5     # 5 cells, nom 18V
    if   V >= 4.20:   cap = 100
    elif V >= 4.15:   cap = 95
    elif V >= 4.11:   cap = 90
    elif V >= 4.08:   cap = 85
    elif V >= 4.02:   cap = 80
    elif V >= 3.98:   cap = 75
    elif V >= 3.95:   cap = 70
    elif V >= 3.91:   cap = 65
    elif V >= 3.87:   cap = 60
    elif V >= 3.85:   cap = 55
    elif V >= 3.84:   cap = 50
    elif V >= 3.82:   cap = 45
    elif V >= 3.80:   cap = 40
    elif V >= 3.79:   cap = 35
    elif V >= 3.77:   cap = 30
    elif V >= 3.75:   cap = 25
    elif V >= 3.73:   cap = 20
    elif V >= 3.71:   cap = 15
    elif V >= 3.69:   cap = 10
    elif V >= 3.61:   cap = 5
    else:             cap = 0

    # get median over 9 samples
    VBatList.append(cap)
    VBatList.pop(0 )
    tmpList = []
    tmpList.extend(VBatList)
    tmpList.sort()
    return(tmpList[4])

################################################################################
Vsonar = ADC(Pin(27))
def GetSonar():
    global Sonar
    VsonarCoeff = 9.0
    S = Vsonar.read_u16() / VsonarCoeff
    return int(S)

Vpir = Pin(28, Pin.IN, Pin.PULL_UP)
def GetPIR():
    if Vpir.value() == 1:
        return True
    else:
        return False

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

dataOther = [0] * 6
def GetOtherData():
    global dataOther
    dataOther[0] = SNR
    dataOther[1] = RSSI
    dataOther[2] = GetSonar()
    dataOther[3] = GetVbat()
    
    PIR = GetPIR()
    # Next two bit wise operations only
    if PIR:
        dataOther[4] = set_bit(dataOther[4],0)
    else:
        dataOther[4] = clear_bit(dataOther[4],0)
    dataOther[5] = 0
    return

################################################################################
# Main 
LEDupdate('GreenSolid')

sx.setBlockingCallback(False, cbLoRa)
Scheduler = 0

while True:
    sleep_ms(1)
    Scheduler += 1

    if (Scheduler - 0) % 100 == 0:          #100ms 0ms offset
        ReadGPS()
        
        if NewCmd:
            LEDupdate('BlueSolid')
            NewCmd = False
            vals,ss = DisAssemPkt_C(NewCmdPkt)
            SendCommand(Tuart, ss)

    if (Scheduler - 50) % 100 == 0:          #100ms 0ms offset
        LEDupdate('GreenSolid')

    if (Scheduler - 10) % 100 == 0:         #100ms 10ms offset          
        RecvTelemetry(Tuart)
        pass
            
    if (Scheduler - 20) % 1000 == 0:      
        ReadIMU()
        #print(dataIMU[6],dataIMU[7],dataIMU[8])


    if (Scheduler - 30) % 1000 == 0:      
        collect()

    if (Scheduler - 40) % 500 == 0:  
        GetOtherData()
        #print(dataGPS, dataMOT, dataIMU, dataOther)
        x = AssemPkt_T(dataGPS, dataMOT, dataIMU, dataOther)
        try:
            sx.send(x)      
        except:
            print('Send failed')
