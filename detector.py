import cv2 as cv 
import numpy as np 

#Reading from index of connected camera
cap = cv.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:

    ret,img=cap.read()
    
    cap.imshow('Video', img)
    
    if(cap.waitKey(10) & 0xFF == ord('b')):
        break

cap.release()
cap.destroyAllWindows()