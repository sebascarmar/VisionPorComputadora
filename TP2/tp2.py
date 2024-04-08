#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2

img =cv2.imread('hoja.png',0)



for row in range(len(img)):
    for col in range(len(img[row])):
        if img[row][col] < 240:
            img[row][col] = 0 


cv2.imwrite('resultado.png', img)
