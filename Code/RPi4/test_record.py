from picamera2.encoders import H264Encoder, JpegEncoder
from picamera2 import Picamera2
from picamera2.outputs import FfmpegOutput
import time
from libcamera import Transform

F180 = Transform(hflip=True, vflip=True)


picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={'size': (700, 500)},  transform=F180)
picam2.configure(video_config)

#encoder = JpegEncoder()
encoder = H264Encoder()
#output = "test1.h264"
output = FfmpegOutput("walk1.mp4", audio=False)

picam2.start_recording(encoder, output)
time.sleep(120)
picam2.stop_recording()



