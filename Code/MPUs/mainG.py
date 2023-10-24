################################################################################
# Roverling Mk II - Telemetry Gateway
print('Roverling Mk II - Gateway main.py on RP2 Pico W')

from time import sleep_ms
import network
from umqttsimple import MQTTClient

from sx1262 import SX1262
from Packets import AssemPkt_T, DisAssemPkt_T, AssemPkt_C, DisAssemPkt_C

# LoRa
sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=3, irq=20, rst=15, gpio=2)
sx.begin(freq=920, bw=250.0, sf=9, cr=5, syncWord=0x12,
         power=22, currentLimit=140.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)

# WiFi
from Secrets import wifi_ssid, wifi_password
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    sleep_ms(1000)
print("Connected to WiFi")

# MQTT
MQTTClientID =      'RV01'
MQTTBroker =        '192.168.2.100'
from Secrets import MQTTUser, MQTTPassword

TopicBase = 'DEV/RV/'

def Publish(topic, mess):
    try:
        client.publish(TopicBase + topic, mess, False)
    except:
        print('MQTT Pub fail')
        client.connect()

def MQTT_cb(topic, msg):
    print(topic, msg)

client = MQTTClient(MQTTClientID, MQTTBroker, user=MQTTUser, password=MQTTPassword)
client.connect()
client.set_callback(MQTT_cb)

client.subscribe('DEV/RV/cmd')

while True:
    msg, err = sx.recv()
    snr = sx.getSNR()
    rssi = sx.getRSSI()
    #print('SNR:',snr,' RSSI:', rssi, 'PKT: ', end='')
    if len(msg) > 0:
        if err !=  0:
            error = SX1262.STATUS[err]
            print('LoRa Recv Error ',error)
        else:
            y = DisAssemPkt_T(msg)
            x = str(y) + ',' + str(snr) + ',' + str(rssi)
            Publish('Packet', x)
            print(x)
            '''print(y)
            Publish('Position', y[1])
            Publish('Quality', str(y[2]))
            Publish('NumSats', str(y[3]))
            Publish('Accuracy', str(y[4]))
            Publish('Altitude', str(y[5]))
            Publish('LeftVel', str(y[6]))
            Publish('RightVel', str(y[7]))
            Publish('LeftCur', str(y[8]))
            Publish('RightCur', str(y[9]))
            Publish('LeftPWM ', str(y[10]))
            Publish('RightPWM', str(y[11]))
            Publish('ch1', str(y[12]))
            Publish('ch2', str(y[13]))
            Publish('ch3', str(y[14]))
            Publish('ch4', str(y[15]))
            Publish('ch5', str(y[16]))
            Publish('ch6,', str(y[17]))
            Publish('AccelX', str(y[18]))
            Publish('AccelY', str(y[19]))
            Publish('AccelZ', str(y[20]))
            Publish('GyrolX', str(y[21]))
            Publish('GyroY', str(y[22]))
            Publish('GyroZ', str(y[23]))
            Publish('MagX', str(y[24]))
            Publish('MagY', str(y[25]))
            Publish('MagZ', str(y[26]))
            Publish('Temp', str(y[27]))
            Publish('Pressure', str(y[28]))
            Publish('RoverSNR', str(y[29]))
            Publish('RoverRSSI', str(y[30]))
            Publish('Sonar', str(y[31]))
            Publish('BatPercent', str(y[32]))
            Publish('GatewaySNR', str(snr))
            Publish('GatewayRSSI', str(rssi))
            
            Publish('B1 - PIR', str(y[33]))
            Publish('B2', str(y[34]))
            '''
            try:
                client.check_msg()
            except:
                print('MQTT Check fail')
                client.connect()

            sleep_ms(100)
            x = AssemPkt_C(123, 0x02, 4, 44, 1.2, 1.3)
            sx.send(x)   



