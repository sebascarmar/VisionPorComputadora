#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2
import numpy as np
#from matplotlib import pyplot as plt
#import pylab as pl


######################## FUNCIONES #######################

def translate(image, x, y):
    (h,w) = (image.shape[0], image.shape[1])

    M = np.float32([[1,0,x],
                    [0,1,y]])

    shifted = cv2.warpAffine(image, M, (w,h))

    return shifted

########################## MAIN ##########################

img = cv2.imread("./../TP2/hoja.png", cv2.IMREAD_GRAYSCALE)

dst = translate(img, x=100, y=100)

#pl.gray(), pl.axis('equal'), pl.axis('off')
#plt.subplot(121), plt.imshow(img), plt.title('Input')
#plt.subplot(122), plt.imshow(dst), plt.title('Output')
#plt.show()

while(1):
    cv2.imshow('Input', img)
    cv2.imshow('Output', dst)

    k = cv2.waitKey(1) & 0xFF
    if(k == 27):
        break
