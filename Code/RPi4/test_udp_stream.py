#!/usr/bin/python3
# from VLC Viewer udp/h264://@:10001
# doesn't apper much faster, haven't tried too hard to get ffplay working

import socket
import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from libcamera import Transform

F180 = Transform(hflip=True, vflip=True)


picam2 = Picamera2()
video_config = picam2.create_video_configuration(transform=F180)
picam2.configure(video_config)
encoder = H264Encoder()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(('192.168.2.1', 10001))
    stream = sock.makefile("wb")
    picam2.start_recording(encoder, FileOutput(stream))
    
    while True:
        pass
    
    time.sleep(2000)
    picam2.stop_recording()
