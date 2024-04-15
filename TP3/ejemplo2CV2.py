#!/usr/bin/env python3
#-*-coding:utf-8-*-


import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('img', gris)
    
    if( (cv2.waitKey(1) & 0xFF) == ord('q') ):
        break

cap.release()
cv2.destroyAllWindows()



