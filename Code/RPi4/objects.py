# Works ok, very slow on video, all procs at 100%
#To install OpenCV I followed these steps (not my own)
#sudo apt install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
#sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
#sudo apt install libxvidcore-dev libx264-dev
#sudo apt install libgtk2.0-dev
#sudo apt install libatlas-base-dev gfortran
#sudo apt install python3-opencv
#sudo apt install openvc-data
#sudo apt install ffmpeg

resX, resY = 960, 540   # 16:9

import cv2
cv2.startWindowThread()

from picamera2 import Picamera2
picam2 = Picamera2()

from libcamera import Transform
F180 = Transform(hflip=True, vflip=True)

picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (resX, resY)}, transform=F180))
picam2.start()

classNames = []
classFile = "/home/rover/Desktop/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/rover/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/rover/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(resX, 540)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms) 
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects: 
                if confidence * 100 > 66:
                    objectInfo.append([box,className])
                    if (draw):
                        cv2.rectangle(img,box,color=(0,255,0),thickness=1)
                        cv2.putText(img,classNames[classId-1].upper(),(box[0]+5,box[1]+30),
                            cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)
                        cv2.putText(img,str(int(confidence*100))+'%',(box[0]+5,box[1]+15),
                            cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)

    return img,objectInfo

while True:
        img = picam2.capture_array()
        result, objectInfo = getObjects(img,0.45,0.2)
        cv2.imshow("Output",img)
        cv2.waitKey(1)
