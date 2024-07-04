#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2
import sys

# Verifica que se ingrese por línea de comandos el archivo de vídeo de entrada
if(len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    print('Ingrese un archivo de vídeo como argumento')
    sys.exit(0)

# Abre el vídeo de entrada con openCV
cap       = cv2.VideoCapture(filename)

# Parámetros del vídeo de entrada
fourcc    = cv2.VideoWriter_fourcc('M','J','P','G') #Formato
fps       = cap.get(cv2.CAP_PROP_FPS)
alto      = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
ancho     = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Configuración del archivo de salida
out       = cv2.VideoWriter('videoOut.avi', fourcc, fps, (ancho,alto))

# Tiempo entre frames del vídeo de entrada
delay     = int((1/fps)*1000) # ms

while( cap.isOpened() ):
    (ret,img) = cap.read()

    if( ret is True ):
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        out.write(img)
        cv2.imshow('Mi video', img)
        if( (cv2.waitKey(delay) & 0xFF) == 27 ):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
