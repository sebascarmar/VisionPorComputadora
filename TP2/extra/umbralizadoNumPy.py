#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2

img = cv2.imread('../hoja.png',0)

thr = 240

img[img>=thr] = 255
img[img< thr] = 0

cv2.imwrite('resultado_numpy.png', img)
