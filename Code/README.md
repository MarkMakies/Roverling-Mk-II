Which code goes into which MPU...

## Motion Processor Processor  
###### (MicroPython v1.20.0 on 2023-04-26; Raspberry Pi Pico with RP2040)

Works independently of other modules.  Can use RC to control without any other modules.
On RC toggle FLAPS to put into RC mode.  Onboard LED will change from steady green to flashing pink.
Ensure throttle is at min first.  Ailerons control steering, elevator controls camera tilt.  GEAR
puts it into reverse mode.

	MPU/mainM.py 			rename to main.py
	MPU/Comms.py                 	inter-MPU Comms
	MPU/QuadDec.py			Motor quadrature decoder (PIO/SM based)
	MPU/RCinterface.py  		6 channel RC interface (interrupt based)

## Telemetry Processor 
###### (MicroPython v1.20.0 on 2023-04-26; Raspberry Pi Pico with RP2040)

Aggregates ALL data from platform for telemetery transmission over LoRa at around 1800bps.  Accepts
LoRa commands. Telemetry includes:

	GPS: 		quality, number satellites, accuracy, altitude, lat & long with 7 decimal places precision
	IMU: 		acceleration (X,Y,Z), gyroscope (X, Y, Z), magnetometer (X, Y, Z), temperature, pressure
	Locomotion: 	velocity (L/R), torque/current (L/R), power delivered (L/R)
	RC: 		6 channels, 0 to 100%
	Platform: 	PIR, sonar range, battery level, status bits
	Comms:  	RSSI & SNR for both Roverling and Base Station ends

&nbsp;
 
	MPU/mainT.py 			rename to main.py
	MPU/GPS.py			Configure and then read GPS module data
	MPU/IMU.py			Intertial measurement unit interface
	MPU/Comms.py			inter-MPU Comms
	MPU/Packets.py			telemetry and control LoRa packet assembly and disassembly
	MPU/Secrets.py			modify and rename Secret_Example.py to Secrets.py
		
	MPU/lib/_sx126x.py 		LoRa drivers from https://github.com/ehong-tl/micropySX126X/tree/master
	MPU/lib/sx1262.py		LoRa drivers from https://github.com/ehong-tl/micropySX126X/tree/master
	MPU/lib/sx126x.py 		LoRa drivers from https://github.com/ehong-tl/micropySX126X/tree/master

## Telemetry Gateway Processor  
###### (MicroPython v1.20.0 on 2023-04-26; Raspberry Pi Pico W with RP2040)

Provides a gateway for Roverling LoRa commands and telemetry to MQTT message broker over WiFi.  Onboard LED
flashes blue when commands are received.  A sigle message is delivered twice a second, and looks a lot like this. (On MQTT Explorer): 
(3172, '-37.0000000, 144.0000000', 1, 4, 3.0, 640.4, 0.0, 0.0, 0.039, 0.043, 0, 0, 10, 50, 51, 51, 9, 10, 0.013, -0.037, 1.015, 0, 0, 0, 0.034, -0.037, 0.455, 19.734, 944.5, 10.25, -42.0, 384, 0, 0, 0, 11.0, -45.0)
	
	MPU/mainG.py 			rename to main.py
	MPU/Packets.py			telemetry and control LoRa packet assembly and disassembly
	MPU/Secrets.py			modify and rename Secret_Example.py to Secrets.py
	
	MPU/lib/_sx126x.py 		LoRa drivers from https://github.com/ehong-tl/micropySX126X/tree/master
	MPU/lib/sx1262.py		LoRa drivers from https://github.com/ehong-tl/micropySX126X/tree/master
	MPU/lib/sx126x.py 		LoRa drivers from https://github.com/ehong-tl/micropySX126X/tree/master
	
	MPU/lib/umqttsimple.py		MQTT module from https://pypi.org/project/micropython-umqtt.simple/#files

