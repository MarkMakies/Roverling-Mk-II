################################################################################
# Roverling Mk II - Packets.py
# Packet assembly / disassembly / compression / encryption
# Need to pack telemetry data as tight as possible.  Most fields will fit into
# 2 bytes.  This has reduced struct.pack size from 106 bytes to 58 (now 64)
# also encrypting so I'm not advertising my exact location to the world

import struct
from cryptolib import aes

char48 = b'1234567890oplmjuyhgliughuxcdhgfjsddsfgreatgadefg'

PktFmt_T = 'HffBHH6h6b9h2H6B'                 # 64 bytes
PktFmt_C = '4H2f'

from Secrets import key_T, key_C

def AssemPkt_T(dataGPS, dataMOT, dataIMU, dataOther):
    # GPS time - now seconds past the hour (unsigned int16)
    SecondsPastHour = (int(dataGPS[0][2:4])*60) + (int(dataGPS[0][4:6])*1)
    # Decimal portion only of degrees
    Latitude, Longitude = dataGPS[1],dataGPS[2]
    # encode quality in top 3 bits and number of sats in bottom 5 bits (byte)
    QualSats = (dataGPS[3] << 5) + dataGPS[4]
    # accuracy, in decimeters (unsigned int16)
    Accuracy = int( dataGPS[5] * 10)
    # altitude, in decimeters (unsigned int16)
    Altitude = int( dataGPS[6] * 10)

    # left / right velocity in mm/sec (signed int16)
    LeftVel, RightVel = int(dataMOT[0] * 1000) ,int(dataMOT[1] * 1000)
    # l / r motor current in mA (unsigned int16)
    LeftCur, RightCur = int(dataMOT[2] * 1000) ,int(dataMOT[3] * 1000)
    # l / r PWM, divided by two so we can add sign for direction (signed int16)
    LeftPWM, RightPWM = int(dataMOT[4] / 2) ,int(dataMOT[5] / 2)
    # RC channels (byte)
    # dataMOT[6..11]

    # Accel in mg (signed int16)
    AccelX, AccelY, AccelZ = int(dataIMU[0]*1000),int(dataIMU[1]*1000),int(dataIMU[2]*1000)
    # Gyro in dps (signed int16)
    GyrolX, GyroY, GyroZ = int(dataIMU[3]),int(dataIMU[4]),int(dataIMU[5])
    # Magnetometer in mG (signed int16)
    MagX, MagY, MagZ = int(dataIMU[6]*1000),int(dataIMU[7]*1000),int(dataIMU[8]*1000)
    # temp mill deg celcius (unsigned int16)
    Temp = int(dataIMU[9]*1000)
    # Pressure =hPa * 10 (unsigned int16)
    Pressure = int(dataIMU[10]*10)

    # Last Received SNR dB (char) -30 -> +10 scale
    SNR = int((dataOther[0]+ 30) * 4)
    # Last RSSI dBm (char) -130 -> -30 scale
    RSSI = int((dataOther[1]+ 130) * 2)
    # Sonar distance 200mm - 7650mm (8192 -> 256, char)
    Sonar =  int(dataOther[2] / 32)
    # BatPercent % (char)
    BatPercent = int(dataOther[3])
    # Bits * 16
    # dataOther[4..5]

    ss = (struct.pack(PktFmt_T, SecondsPastHour, Latitude, Longitude, QualSats,
        Accuracy, Altitude, LeftVel, RightVel, LeftCur, RightCur, LeftPWM, RightPWM,
        dataMOT[6],dataMOT[7],dataMOT[8],dataMOT[9],dataMOT[10],dataMOT[11],
        AccelX, AccelY, AccelZ, GyrolX, GyroY, GyroZ, MagX, MagY, MagZ, Temp, Pressure,
        SNR, RSSI, Sonar, BatPercent, dataOther[4], dataOther[5] ))

    cipher = aes(key_T, 1)
    ee = cipher.encrypt(ss)
    return ee

def DisAssemPkt_T(pkt):
    cipher = aes(key_T, 1)
    try:
        ee = cipher.decrypt(pkt)
    except:
        return 'Decryption Error'
    else:
        pk = struct.unpack(PktFmt_T, ee)
        
        SecondsPastHour = pk[0]
        LatDegrees, LongDegrees = -37, 144
        LatMinutes, LongMinutes = pk[1],pk[2]
        Quality = (pk[3] & 0xe0) >> 5
        NumSats = pk[3] & 0x1f
        Accuracy = pk[4] / 10
        Altitude = pk[5] / 10

        LeftVel, RightVel = pk[6] / 1000, pk[7] / 1000
        LeftCur, RightCur = pk[8] / 1000, pk[9] / 1000
        LeftPWM, RightPWM = pk[10] * 2, pk[11] * 2
        ch1,ch2,ch3,ch4,ch5,ch6 = pk[12],pk[13],pk[14],pk[15],pk[16],pk[17],

        AccelX, AccelY, AccelZ = pk[18] / 1000, pk[19] / 1000, pk[20] / 1000
        GyrolX, GyroY, GyroZ = pk[21],pk[22],pk[23]
        MagX, MagY, MagZ = pk[24] / 1000, pk[25] / 1000, pk[26] / 1000 
        Temp = pk[27] / 1000
        Pressure = pk[28] / 10

        SNR = (pk[29] / 4) - 30
        RSSI = (pk[30] / 2) - 130
        Sonar = pk[31] * 32
        BatPercent = pk[32]
        B1, B2 = pk[33], pk[34]

        tt = (SecondsPastHour, 
            str(LatDegrees)+str(LatMinutes)[1:]+', '+ str(LongDegrees)+str(LongMinutes)[1:], 
            Quality, NumSats, Accuracy, Altitude,
            LeftVel, RightVel,LeftCur, RightCur,LeftPWM, RightPWM,ch1,ch2,ch3,ch4,ch5,ch6,
            AccelX, AccelY, AccelZ, GyrolX, GyroY, GyroZ, MagX, MagY, MagZ, Temp, Pressure,
            SNR, RSSI, Sonar, BatPercent, B1, B2)

        return(tt)

def AssemPkt_C(SecCheck, OpCode, int1, int2, float1, float2):
    ss = struct.pack(PktFmt_C, SecCheck, OpCode, int1, int2, float1, float2)
    cipher = aes(key_C, 1)
    ee = cipher.encrypt(ss)
    return ee

def DisAssemPkt_C(pkt):
    cipher = aes(key_C, 1)
    try:
        ee = cipher.decrypt(pkt)
    except:
        return 'Decryption Error'
    else:
        pk = struct.unpack(PktFmt_C, ee)
        
        SecCheck = pk[0]
        OpCode = pk[1]
        int1, int2 = pk[2], pk[3]
        float1, float2 = pk[4], pk[5]

        values = SecCheck, OpCode, int1, int2, float1, float2
        string = (str(pk[0]) + ',' + str(pk[1]) + ',' + str(pk[2]) + ',' +
                str(pk[3]) + ',' + str(pk[4]) + ',' + str(pk[5]))
        return(values, string)
