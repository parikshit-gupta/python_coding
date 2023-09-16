import cv2
import time

width=int(input("enter the widht of a single frame: "))
height=int(input("enter the height of a single frame: "))

cam_obj=cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam_obj.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam_obj.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam_obj.set(cv2.CAP_PROP_FPS, 30)
cam_obj.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

x=0
y=0
c=0
rows= int (1280/width)
columns= int(720/height)
n= rows*columns
while True:
    bool_val, frame=cam_obj.read()
    if (c==n):
        if(cv2.waitKey(1)& 0xff ==ord('q')):
            break
        
        continue
    for i in range(1,rows+1):
        for j in range(1, columns+1):
            cv2.imshow(('MCW%d' %(c)), frame)
            cv2.moveWindow(('MCW%d' %(c)), x,y)
            x=x+width
            c=c+1
        y=y+height
        

    
cv2.release()

