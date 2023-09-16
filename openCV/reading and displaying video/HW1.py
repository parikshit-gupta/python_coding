#moving display windows around :)

import cv2
from time import sleep
print("hello pz")
cam_obj = cv2.VideoCapture(0)
x=0
y=0
while True:
    bool_val, frame = cam_obj.read()
    greyframe=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('webcam1', frame)
    cv2.imshow('webcam2', greyframe)
    cv2.imshow('webcam3', greyframe)
    cv2.imshow('webcam4', greyframe)

    cv2.moveWindow('webcam1', 0,0)
    cv2.moveWindow('webcam2', 620,0)
    cv2.moveWindow('webcam3', 0,190)
    cv2.moveWindow('webcam4', 620,190)
    #x=x+10
    #y=y+10
    print(y)
    sleep(0.1) #takes time in seconds
    if (cv2.waitKey(1) & 0xff == ord('q')): #0xff is used to convert across the UNICODE encoding in string used in python
        break

cam_obj.release()