#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2
import numpy as np
#from matplotlib import pyplot as plt
#import pylab as pl


######################## FUNCIONES #######################

def flip(image, mode):
    modes = {'x':0, 'y':-1, 'b':-1}

    if( mode not in modes.keys() ):
        return img
    
    flipped = cv2.flip(img, modes[mode])

    return flipped
    

########################## MAIN ##########################


img = cv2.imread("./../TP2/hoja.png", cv2.IMREAD_GRAYSCALE)

dst = flip(img, mode='y')

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
