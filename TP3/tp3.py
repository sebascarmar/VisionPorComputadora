#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2
import sys

if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Ingrese un archivo de vídeo como argumento')
    sys.exit(0)

cap       = cv2.VideoCapture(filename)

fourcc    = cv2.VideoWriter_fourcc('X','V','I','D') #Formato
fps       = cap.get(cv2.CAP_PROP_FPS)
alto      = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
ancho     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
out       = cv2.VideoWriter('videoOut.mkv', fourcc, fps, (ancho,alto))

delay     = int((1/fps)*1000)

while( cap.isOpened() ):
    (ret,img) = cap.read()

    if( ret is True ):
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        out.write(img)
        cv2.imshow('Mi video', img)
        if( (cv2.waitKey(delay) & 0xFF) == ord('q') ):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
