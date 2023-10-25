#!/usr/bin/python3
# super slow

import time
from picamera2 import Picamera2, Preview
from libcamera import Transform

picam2 = Picamera2()
config = picam2.create_preview_configuration(main= {"size": (640, 480)}, transform=Transform(hflip=1,vflip=1) )
picam2.configure(config)


picam2.start_preview(Preview.QTGL)
picam2.start()


time.sleep(60)
