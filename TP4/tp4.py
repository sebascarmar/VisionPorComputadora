# El programa debe permitir dibujar un rectángulo en la imagen. Luego, al presionar:
#   'g'  : debe guardar el recorte de imagen seleccionado.
#   'r'  : debe eliminar la selección y permitir volver a seleccionar.
#   'esc': debe salir del programa


import cv2
import numpy as np


######################## FUNCIONES #######################

def select_image(event, x, y, flags, param):
    global xi, yi, xf, yf, drawing, mode, img
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (xi, yi) = (x, y)
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            img = img_aux.copy()
            (xf, yf) = (x, y)
            cv2.rectangle(img, (xi,yi), (x,y), (255,0,255), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


########################## MAIN ##########################

drawing  = False 
mode     = True 
(xi, yi) = (-1, -1)
(xf, yf) = (-1, -1)

img     = cv2.imread ('../TP2/hoja.png', 1)
img_aux = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', select_image)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if(k == ord('r')):
        img = img_aux.copy()
    elif(k == ord('g')):
        cv2.imwrite('resultado.png', img_aux[yi:yf,xi:xf])
    elif(k == 27):
        break

cv2.destroyAllWindows()




