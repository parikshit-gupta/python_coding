import cv2
import time
width=1280
lenght= 720
cam_obj=cv2.VideoCapture(0, cv2.CAP_DSHOW)

#setting widht height, fps of the display video
cam_obj.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam_obj.set(cv2.CAP_PROP_FRAME_HEIGHT, lenght)
cam_obj.set(cv2.CAP_PROP_FPS, 30)
#setting up codec for our video stream
cam_obj.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    bool_val, frame= cam_obj.read()
    cv2.imshow('myWebcam', frame)
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('myWebcam2', gray_frame)
    if (cv2.waitKey(1) & 0xff ==ord('q')):
        break
cv2.release()

