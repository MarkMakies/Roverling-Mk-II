#!/usr/bin/python3
# from VLC Viewer tcp/h264://192.168.2.20:10001

# recommended
# ffplay tcp://192.168.2.20:10001 -vf "setpts=N/30" -fflags nobuffer -flags low_delay -framedrop
# libcamera-vid --nopreview --inline --width 1536 --height 864 --rotation 180 --listen -t 0 -o tcp://0.0.0.0:10001

# this works for me
# ffplay tcp://192.168.2.20:10001 -fflags nobuffer -flags low_delay -framedrop

import socket
import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from libcamera import Transform

F180 = Transform(hflip=True, vflip=True)

picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={'size': (960, 540)},  transform=F180)
#picam2.align_configuration(video_config)
#print(video_config)

picam2.configure(video_config)
encoder = H264Encoder()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("0.0.0.0", 10001))
    sock.listen()

    picam2.encoders = encoder

    conn, addr = sock.accept()
    stream = conn.makefile("wb")
    encoder.output = FileOutput(stream)
    picam2.start_encoder()
    picam2.start()
    
    time.sleep(200000)
    picam2.stop()
    picam2.stop_encoder()
    conn.close()
