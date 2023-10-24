################################################################################
# Roverling Mk II - Telemetry & Control inter-MPU Comms.py 

dataMOT = [0] * 12
prevTelemString = ' '

dataCMD = [0] * 6
prevCommandString = ' '

def CheckPacket(ss):
    # GPS and inter-MPU only use (sentence based)
    payload = bytes(ss[1:ss.find('*')], 'utf-8')
    checksum = bytes(ss[ss.find('*')+1:ss.find('*')+3], 'utf-8')
    csum = 0
    for char in payload:
        csum ^= char
    return bytes("{:02x}".format(csum).upper(), 'ascii') == checksum

def RecvTelemetry(uu):  
    global dataMOT
    global prevTelemString

    x = uu.read()
    if x is not None:
        if x != prevTelemString:
            try:
                ss = x.decode('UTF-8')
            except:
                print('Packet decode error')
            else:
                if CheckPacket(ss):
                    if ss.find('$TELMM') == 0:
                        try:
                            Lvel = float(ss.split(',')[1])
                            Rvel = float(ss.split(',')[2])
                            Lcur = float(ss.split(',')[3])
                            Rcur = float(ss.split(',')[4])
                            Lpwm = float(ss.split(',')[5])
                            Rpwm = float(ss.split(',')[6])
                            Ch1= int(ss.split(',')[7])
                            Ch2= int(ss.split(',')[8])
                            Ch3= int(ss.split(',')[9])
                            Ch4= int(ss.split(',')[10])
                            Ch5= int(ss.split(',')[11])
                            Ch6= int(ss.split(',')[12])
                        except:
                            print('Data conversion error (Mot/RC)')
                        else:
                            dataMOT[0] = Lvel
                            dataMOT[1] = Rvel
                            dataMOT[2] = Lcur
                            dataMOT[3] = Rcur
                            dataMOT[4] = Lpwm
                            dataMOT[5] = Rpwm
                            dataMOT[6] = Ch1
                            dataMOT[7] = Ch2
                            dataMOT[8] = Ch3
                            dataMOT[9] = Ch4
                            dataMOT[10] = Ch5
                            dataMOT[11] = Ch6
                            prevTelemString = x
                            return True
                    else:
                        print('OTHER:', ss)
                else:
                    pass    #Telemetry check sum error
    return False

def SendTelemetry(uu, dataM, dataR):
    ss = ('TELMM' + ',' + str(dataM[0]) + ',' + str(dataM[1]) + ',' + str(dataM[2]) + ',' 
        + str(dataM[3]) + ',' + str(dataM[4]) + ',' + str(dataM[5]) + ',' 
        + str(dataR[0]) + ',' + str(dataR[1]) + ',' + str(dataR[2]) + ',' 
        + str(dataR[3]) + ',' + str(dataR[4]) + ',' + str(dataR[5]) + ',')

    payload = bytes(ss, 'utf-8')
    checksum = 0
    for char in payload:
        checksum ^= char
    x = (b'$' + payload + b'*' +  bytes("{:02x}".format(checksum).upper(), 'ascii') 
        + b'\r\n')
    uu.write(x) 

def RecvCommand(uu):  
    global dataCMD
    global prevCommandString

    x = uu.read()
    if x is not None:
        if x != prevCommandString:
            try:
                ss = x.decode('UTF-8')
            except:
                print('Packet decode error cmd')
            else:
                if CheckPacket(ss):
                    if ss.find('$CMDMM') == 0:
                        try:
                            SecCheck = int(ss.split(',')[1])
                            OpCode = int(ss.split(',')[2])
                            int1 = int(ss.split(',')[3])
                            int2 = int(ss.split(',')[4])
                            float1 = float(ss.split(',')[5])
                            float2 = float(ss.split(',')[6])

                        except:
                            print('Data conversion error (Command)')
                        else:
                            dataCMD[0] = SecCheck
                            dataCMD[1] = OpCode
                            dataCMD[2] = int1
                            dataCMD[3] = int2
                            dataCMD[4] = float1
                            dataCMD[5] = float2

                            prevCommandString = x
                            return True
                    else:
                        print('OTHER:', ss)
                else:
                    pass        # Telemetry check sum error
    return False

def SendCommand(uu, Cstr):           # just bytes passed straight through
    ss = ('CMDMM' + ',' + Cstr + ',')
    payload = bytes(ss, 'utf-8')
    checksum = 0
    for char in payload:
        checksum ^= char
    x = (b'$' + payload + b'*' +  bytes("{:02x}".format(checksum).upper(), 'ascii') 
        + b'\r\n')
    uu.write(x) 
