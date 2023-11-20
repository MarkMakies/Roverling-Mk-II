## Roverling Mk II
# A cheap multipurpose mobile robotic platform for research, development, education and fun
Follow #Roverling on Instagram for project progress.   All design files, schematics & code available [here](https://core-electronics.com.au/projects/roverling-mk2/).

### STAGE 1 - Mecha Design July 2023

![cad](https://github.com/MarkMakies/Roverling-Mk-II/assets/105891859/a6fa1e8c-58e0-44ce-b056-a00f4ce3b745)

### STAGE 1 - Complete Aug 2023

![rv2a](https://github.com/MarkMakies/Roverling-Mk-II/assets/105891859/1ff963ae-4144-4854-b0a7-fd3813da80cb)

### Stage 2 - Tronics design wish list Sep 2023

![rv2b](https://github.com/MarkMakies/Roverling-Mk-II/assets/105891859/7dcae563-0723-4818-ae79-13c0630627ed)

### Stage 2 - MPU code development and electronics complete Oct 2023

![IMG_1045](https://github.com/MarkMakies/Roverling-Mk-II/assets/105891859/53bcc2d5-a095-483d-891b-787f3cfac39f)

### Stage 3 - GUI complete as well as LoRa /WiFi /MQTT gateway.  

![Screenshot_2023-10-24_15-35-30](https://github.com/MarkMakies/Roverling-Mk-II/assets/105891859/2d0717cf-a4fb-4b08-a163-27af71d6e3ab)

## And now, Oct 2023,  writing it all up so others can understand and follow I hope :) 

in progress.....


# Why did I start this project:   

A few months back I created a basic mobile platform using parts from an old 3D printer.  It was fun but not very practical.

I designed Roverling Mark II so I could experiment with a practical, configurable and reliable  mobile platform.  Hopefully one day getting it to do some useful stuff around our bush block, like

      - Searching paddocks for weeds and recording locations.
      - Navigating down a 200m drive to check if the gate is closed.
      - Navigating up the drive 50m to check that the machine shed roller doors are secure.
      - Recording animal sightings on the block.  We’d see up to 50 roos per day on our block.
      - It would be good to identify and scare deer away from our olive grove.
      - And a friend already wants to mount a metal detector and do automatic scanning of a large area.

Anyway, to that end, here is the complete design and everything you need to know to make your own or any variation.  As much as possible I’ve kept the cost down to a minimum, reused some older parts and printed as much as possible.


This is a current work in progress.  At some stage I needed to draw the line and write something up before it gets too big.  So these are the current working and operational specifications

    
     - 440 mm long x 350 mm wide, 250 mm max height, 200 mm nominal platform height
     - 3.5 kg without battery, uses an 18V power tool battery
     - Up to 22 satellite GNSS receiver, augmentation using SBAS, 1Hz updates
     - IMU: 3x accel, 3x gyro, magnetometer, pressure
     - 2.4Ghz 6 channel RC receiver and decoder, with diverse receiver
     - 2 channel motor quadrature decoders 
     - 2 channel motor current sensors (effectively torque sensors)
     - Sonar, ranger
     - 915 Mhz LoRa module.  Comms at 1800 bps,  64 byte telemetry packet, 16 byte command packet, encrypted, super reliable
      LoRa base station, which is effectively my MQTT gateway for telemetry and commands back
     - Mapping module runs on desktop from MQTT feed to produce realtime tracking info overlaid on an image (for me an old NearMap screenshot).
      On board RPi 4B w/ 4G running the latest OS with a camera 3 module.  

All the 3D design is done in FreeCAD and all the slicing and printing on a Prusa platform.  As well as the actual design files, I’ve also made available stl model files, g-code files and Prusa project files for all parts.

The schematic is done with KiCAD.  I used mixed prototyping methods and no PCB has been designed (yet) so you will need a fair understanding of how to layout and wire correctly.

All the code is in python.  I’ve pretty much written my own drivers for all of the low level stuff except the sx1262 suite for LoRa and MQTT.  I’ve tried to document as much as possible.  

