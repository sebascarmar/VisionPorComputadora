#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2

img = cv2.imread('../hoja.png',0)


thr = 240
(retval,dst) = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY) # BINARY_INV, TRUNC, TOZERO, TOZERRO_INV

cv2.imwrite('resultado_opencv.png', dst)


(retval,dst) = cv2.threshold(img, int(), 255, cv2.THRESH_OTSU) # TRIANGLE

print("Umbral calculado por la librería: ", retval)
cv2.imwrite('resultado_opencv_otsu.png', dst)
