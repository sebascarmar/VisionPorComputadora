#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2
import numpy as np
#import matplotlib.pyplot as plt
#import pylab as pl

######################## FUNCIONES #######################

def rotate(image, angle, center=None, scale=1.0):
    (h,w) = image.shape[:2]

    if center is None:
        center = (w/2, h/2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, M, (w,h))

    return rotated

########################## MAIN ##########################

img = cv2.imread("./../TP2/hoja.png", cv2.IMREAD_GRAYSCALE)

dst = rotate(image=img, angle=15, center=(0,0), scale=1)

while(1):
    cv2.imshow('Input', img)
    cv2.imshow('Output', dst)

    k = cv2.waitKey(1) & 0xFF
    if(k == 27):
        break

#pl.gray(), pl.axis('equal'), pl.axis('off')
#plt.subplot(121), plt.imshow(img), plt.title('Input')
#plt.subplot(122), plt.imshow(dst), plt.title('Output')
#plt.show()

