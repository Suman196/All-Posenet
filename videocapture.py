import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3,1920)# 3 for the width, and 4 for the height
    cap.set(4,1080)

def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)

def change_res(width,height):
    cap.set(3,width)
    cap.set(4,height)

change_res(6000,3000)# change resolution

while(True):
    # Capture frame by frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if(cv2.waitKey(20) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()