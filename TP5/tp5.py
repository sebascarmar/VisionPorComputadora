# el programa debe permitir dibujar un rectángulo en la imagen. luego, al presionar:
#   'g'  : debe guardar el recorte de imagen seleccionado.
#   'e'  : aplica una transformación euclidiana al recorte seleccionado.
#   'r'  : debe eliminar la selección y permitir volver a seleccionar.
#   'esc': debe salir del programa


import cv2
import numpy as np
from matplotlib import pyplot as plt
import pylab as pl
import transform


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

def euclidiana(image, angle, tx, ty):
    aux          = transform.translate(image, x=tx, y=ty)
    tras_and_rot = transform.rotate(aux, angle, center=None, scale=1.0)

    return tras_and_rot
    

########################## MAIN ##########################

drawing  = False 
mode     = True 
(xi, yi) = (-1, -1)
(xf, yf) = (-1, -1)

# Parámetros de transformación
angle  = 45
tras_x = 100
tras_y = 100

# Apertura de la imagen y creación de su copia
img     = cv2.imread ('../TP2/hoja.png', 1)
img_aux = img.copy()

# Seteo de los eventos del mouse
cv2.namedWindow('image')
cv2.setMouseCallback('image', select_image)


while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF

    if(k == ord('r')):   # elimina el rectángulo dibujado
        img = img_aux.copy()

    elif(k == ord('g')): # guarda recorte selccionado
        cv2.imwrite('captura.png', img_aux[yi:yf,xi:xf])

    elif(k == ord('e')): # transformación ecuclidiana
        dst = euclidiana(img_aux[yi:yf,xi:xf], angle, tras_x, tras_y)
        cv2.imwrite('euclidiana.png', dst)

    elif(k == 27):       # sale del bucle con 'esc'
        break

cv2.destroyAllWindows()
