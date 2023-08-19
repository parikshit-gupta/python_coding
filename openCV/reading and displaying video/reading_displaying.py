import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0) #creating camera object (reads data from the camera), '0' indicates camera slot 0.
while True:
    a, frame = cam.read() #reading the camera object, it returns a boolean and a array for the frame
    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('webcam', greyframe) #showing the frame
    cv2.moveWindow('webcam', 0,0)
    # exit program
    if cv2.waitKey(1) & 0xff == ord('q'): #checking for keyboard input every 1ms if 'q' was entered
        break
cam.release() #relesing the camera port occupied by the camera object.
