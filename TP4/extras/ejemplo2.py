import cv2
import numpy as np

blue  = (255,   0,   0)
green = (  0, 255,   0)
red   = (  0,   0, 255)

drawing       = False
mode          = True
xybutton_down = (-1, -1)

######################## FUNCIONES #######################

def dibuja(event, x, y, flags, param):
    global xybutton_down, drawing, mode
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing = True
        xybutton_down = x, y
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            img[:] = 0
            if(mode is True):
                cv2.rectangle(img, xybutton_down, (x,y), blue, -1)
            else:
                cv2.line(img, xybutton_down, (x,y), red, 2)
    elif(event == cv2.EVENT_LBUTTONUP):
        drawing = False

########################## MAIN ##########################

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', dibuja)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if(k == ord('m')):
        mode = not mode
    elif(k == 27):
        break

cv2.destroyAllWindows()

