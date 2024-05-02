import cv2
import numpy as np

def translate(image, x, y):
    (h,w) = (image.shape[0], image.shape[1])

    M = np.float32([[1,0,x],
                    [0,1,y]])

    shifted = cv2.warpAffine(image, M, (w,h))

    return shifted


def rotate(image, angle, center=None, scale=1.0):
    (h,w) = image.shape[:2]

    if( center is None):
        center = (w/2, h/2)

    M = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, M, (w,h))

    return rotated

def flip(image, mode):
    modes = {'x':0, 'y':-1, 'b':-1}

    if( mode not in modes.keys() ):
        return img
    
    flipped = cv2.flip(img, modes[mode])

    return flipped

