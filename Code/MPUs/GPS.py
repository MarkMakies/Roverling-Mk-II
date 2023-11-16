################################################################################
# Roverling Mk II - GPS.py GPS module
#
# 03/09/23  Not enough precision in 32 bit float for calculation of decimal 
#  degrees to better than 8m longitudely.  Will fix by 
#  and transporting only minutes and hard coding degrees at Rx end.
# 25/08/23  ran out of UARTS,reconfiguring to use PIO based UART instead
#  wish I has an extra real one, this has been problematic
#  byte assembly interrupt is being interrupted
# 22/10/23 back to HW based UART - nothing but problems with PIO based
#   implementation.  Now out of UARTs so will probably need to fix so
#   we can talk to RPI4

#from PIO_UART import PIO_UART0_readline, PIO_UART0_write
from machine import Pin, UART
from Comms import CheckPacket

Guart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), timeout=10 )

dataGPS = ['000000.000', 0.0, 0.0, 0, 0, 0, 0]
prevString = ' '

def ReadGPS():
    global dataGPS
    global prevString

    #x = PIO_UART0_readline()
    x = Guart.readline() 

    if not x is None:
        if x != prevString:
            ss = ''.join(chr(i) for i in x)

            if CheckPacket(ss):
                if ss.find('$GNGGA') == 0:  #maybe for GPGGA as well?
                    try:
                        Gutc = (ss.split(',')[1])     
                        dataGPS[0] = Gutc

                        s = ss.split(',')[2]
                        Glattide = float(s[2:9])/60

                        s = ss.split(',')[4]
                        Glongitude = float(s[3:10])/60

                        Gquality = int(ss.split(',')[6])
                        Gnumstats = int(ss.split(',')[7])
                        Gaccuracy = float(ss.split(',')[8])
                        Galtitude = float(ss.split(',')[9])
                    except:
                        #print('ERROR data conversion error (GPS)', ss)
                        pass # usually means no satellite fix yet 
                    else:
                        dataGPS[0] = Gutc
                        dataGPS[1] = Glattide
                        dataGPS[2] = Glongitude         
                        dataGPS[3] = Gquality
                        dataGPS[4] = Gnumstats
                        dataGPS[5] = Gaccuracy
                        dataGPS[6] = Galtitude

                        prevString = x
                        return True
                else:
                    print('ERROR, unexpected response:', ss)
            else:
                print('ERROR failed CheckPacket:',ss)
        else:
            print('ERROR duplicate packet:')

    return False


def WriteGPS(command: bytes):   
    checksum = 0
    for char in command:
        checksum ^= char
    x = b'$' + command + b'*' +  bytes("{:02x}".format(checksum).upper(), 'ascii') + b'\r\n'
    #PIO_UART0_write(x.decode('UTF-8'))
    Guart.write(x.decode('UTF-8')) 

# Configure GPS device MTK3339
# https://cdn-shop.adafruit.com/datasheets/PMTK_A08.pdf  (NOT v11 !)

# Update rate and position fix to 1000 max for SBAS, else max is 200ms 
WriteGPS(b'PMTK220,1000')
WriteGPS(b'PMTK300,1000,0,0,0,0')
# Enable SBAS augmentation: ! only if output rate < 1Hz
WriteGPS(b'PMTK313,1')
# Turn on GGA only
WriteGPS(b"PMTK314,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
# Expect in return, 4x  $PMTK001, with flag set to 3
