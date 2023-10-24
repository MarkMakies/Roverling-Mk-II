################################################################################
# Roverling Mk II - Interface for AltIMU-10 v6 carrier:
#  LSM6DSO Accelerometer/Gyro/Temp
#  LPS22DF Barometer
#  LIS3MDL Magnetometer

from machine import Pin, I2C
import struct

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=100_000)

def DevWrite(addr, reg, data):
    i2c.writeto_mem(addr, reg, data.to_bytes(1, 'little'))

def DevReadInt16(addr, regLSB):
    lsb, msb = i2c.readfrom_mem(addr, regLSB, 2)
    return struct.unpack('<h', bytes([lsb, msb]))[0]

def DevReadInt24(addr, regLSB):
    xlsb, lsb, msb = i2c.readfrom_mem(addr, regLSB, 3)
    return struct.unpack('<I', bytes([xlsb, lsb, msb,0]))[0]

dataIMU = [0.1] * 11
prevIMU = dataIMU[:]

################################################################################
# Accelerometer/Gyro/Temp

AccelAddr   = 0x6b 
A_CTRL1_XL  = 0x10
A_CTRL2_G   = 0x11
A_OUT_TEMP  = 0x20 
A_OUTX_G    = 0x22 
A_OUTY_G    = 0x24 
A_OUTZ_G    = 0x26 
A_OUTX_XL   = 0x28 
A_OUTY_XL   = 0x2A 
A_OUTZ_XL   = 0x2C 

OffsetTemp = -480            # determine by testing, raw should == 0 at 25 degC
LinAccelSens4g = 0.122      # mg/LSB 
AngRateSens250dps = 8.75    # mdps/LSB

DevWrite(AccelAddr, A_CTRL1_XL, 0b00111000)    # Activate accel | 52 Hz | 4g | LPF def : 0011 10 00
DevWrite(AccelAddr, A_CTRL2_G, 0b00110000)     # Activate gyro  | 52 Hz | 250 deg/s | def | 0 : 0011 00 0 0

################################################################################
# Magnetometer

MagAddr      = 0x1e
M_CTRL_REG1  = 0x20
M_CTRL_REG2  = 0x21
M_CTRL_REG3  = 0x22
M_CTRL_REG4  = 0x23

M_OUTX    = 0x28 
M_OUTY    = 0x2a 
M_OUTZ    = 0x2c 

GNSens4g    = 6842      # LSB / gauss

DevWrite(MagAddr, M_CTRL_REG1, 0b00110000)    # temp off | med perf | 10Hz 0 | no s-tst : 0 01 100 0 0
DevWrite(MagAddr, M_CTRL_REG3, 0b00000000)    # continous conversion mode
#DevWrite(MagAddr, M_CTRL_REG4, 0b00000100)    # z axis med perf

################################################################################
# Barometer

BaroAddr        = 0x5d     
B_CTRL_REG1     = 0x10
PRESSURE_OUT_XL = 0x28

PressSens = 4096    # LSB/hPA

DevWrite(BaroAddr, B_CTRL_REG1, 0b00011011)    # 0 | 10 Hz | avg 32  : 0 0011 011

################################################################################

def ReadIMU():
    global dataIMU
    global prevIMU

    AccelX = (DevReadInt16(AccelAddr, A_OUTX_XL) * LinAccelSens4g) / 1000
    AccelY = (DevReadInt16(AccelAddr, A_OUTY_XL) * LinAccelSens4g) / 1000
    AccelZ = (DevReadInt16(AccelAddr, A_OUTZ_XL) * LinAccelSens4g) / 1000
    GyroX = (DevReadInt16(AccelAddr, A_OUTX_G) * AngRateSens250dps) / 1000
    GyroY = (DevReadInt16(AccelAddr, A_OUTY_G) * AngRateSens250dps) / 1000
    GyroZ = (DevReadInt16(AccelAddr, A_OUTZ_G) * AngRateSens250dps) / 1000
    Temp = ((DevReadInt16(AccelAddr, A_OUT_TEMP) + OffsetTemp) / 256 ) + 25

    MagX = (DevReadInt16(MagAddr, M_OUTX) / GNSens4g) 
    MagY = (DevReadInt16(MagAddr, M_OUTY) / GNSens4g) 
    MagZ = (DevReadInt16(MagAddr, M_OUTZ) / GNSens4g) 

    Pressure = (DevReadInt24(BaroAddr, PRESSURE_OUT_XL) / PressSens)    # hPa

    dataIMU[0] = AccelX
    dataIMU[1] = AccelY
    dataIMU[2] = AccelZ
    dataIMU[3] = GyroX
    dataIMU[4] = GyroY
    dataIMU[5] = GyroZ

    dataIMU[6] = MagX
    dataIMU[7] = MagY
    dataIMU[8] = MagZ

    dataIMU[9] = Temp
    dataIMU[10] = Pressure

    if dataIMU != prevIMU:
        prevIMU = dataIMU[:]
        return True
    else:
        return False
