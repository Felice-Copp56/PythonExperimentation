import cv2
import os.path
import math


count = 0
videoFile ="XCloud55.mkv"
savepath = 'C:/Users/coppo/Desktop/Università/1_annoCloudComputing/RetiGeografiche/Stadia5-5'
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="frame%d.jpg" % count;count+=1
        cv2.imwrite(filename, frame)
cap.release()
print ("Done!")




