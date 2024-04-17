#!/usr/bin/env python3
#-*-coding:utf-8-*-


import cv2
import sys

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Ingrese un archivo de vídeo como argumento')
    sys.exit(0)


cap = cv2.VideoCapture(filename)

while cap.isOpened():
    ret, frame = cap.read()
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Frame', gris)
    
    if( (cv2.waitKey(33) & 0xFF) == ord('q') ): #1/30fps = 33ms
        break


cap.release()
cv2.destroyAllWindows()



