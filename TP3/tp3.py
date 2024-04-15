#!/usr/bin/env python3
#-*-coding:utf-8-*-


import cv2

cap = cv2.VideoCapture(0)


fps   = cap.get(cv2.CAP_PROP_FPS)
alto  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
ancho = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#ret, frame = cap.read()
#alto,ancho = frame.shape[:2]

cap.release()

print('El valor de fps de la cámara es:', fps)
print('El valor de ancho y alto es de la cámara es:', ancho, 'x', alto)

cv2.destroyAllWindows()


