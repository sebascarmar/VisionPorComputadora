import cv2
import numpy as np

drawing  = False 
mode     = True 
(xi, yi) = (-1, -1)

######################## FUNCIONES #######################

def select_image(event, x, y, flags, param):
    global xi, yi, drawing, mode#, img
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (xi, yi) = (x, y)
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            img_aux = img.copy()
            cv2.rectangle(img_aux, (xi,yi), (x,y), (255,0,255), 2)
            cv2.imshow('image', img_aux )
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


########################## MAIN ##########################

img = cv2.imread ('../TP2/hoja.png', 1)
#img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', select_image)
cv2.imshow('image', img)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if(k == ord('m')):
        mode = not mode
    elif(k == 27):
        break

cv2.destroyAllWindows()




