#!/usr/bin/env python3
#-*-coding:utf-8-*-


import cv2


cap       = cv2.VideoCapture(0)
fourcc    = cv2.VideoWriter_fourcc('X','V','I','D') #Formato
fps       = 33
anchoalto = (640,480)
out       = cv2.VideoWriter('mivideo.mkv', fourcc, fps, anchoalto)

while( cap.isOpened() ):
    (ret,img) = cap.read()

    if( ret is True ):
        out.write(img)
        cv2.imshow('Mi video', img)
        if( (cv2.waitKey(1) & 0xFF) == ord('q') ):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
