# el programa debe permitir dibujar un rectángulo en la imagen. luego, al presionar:
#   'g'  : debe guardar el recorte de imagen seleccionado.
#   'e'  : aplica una transformación euclidiana al recorte seleccionado.
#   's'  : aplica una transformación similaridad al recorte seleccionado.
#   'a'  : aplica una transformación afin, e incrusta imagen en selección de 3 puntos.
#   'r'  : debe eliminar la selección y permitir volver a seleccionar.
#   'p'  : vuelve a mostrar la primer imagen abierta (la hoja en este caso).
#   'esc': debe salir del programa.
#41cmx93.5cm   -> acrílico de la mesa
#22.3cmx29.5cm -> cuaderno
#15cmx15cm     -> placa

import cv2
import numpy as np
import transform


######################## funciones #######################

def sel_cuatro_puntos(event, x, y, flags, param):
    global x1, y1, x2, y2, x3, y3, x4, y4
    global drawing, mode, img, counter 

    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (xi, yi) = (x, y)

    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            if(counter==0):
                (x1, y1) = (x, y)
                cv2.circle(img, (x,y), 2, (255,255,0), -1)
            elif(counter==1):
                (x2, y2) = (x, y)
                cv2.circle(img, (x,y), 2, (255,255,0), -1)
            elif(counter==2):
                (x3, y3) = (x, y)
                cv2.circle(img, (x,y), 2, (255,255,0), -1)
            elif(counter==3):
                (x4, y4) = (x, y)
                cv2.circle(img, (x,y), 2, (255,255,0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if(counter==0):
            (x1, y1) = (x, y)
            cv2.circle(img, (x,y), 2, (255,255,0), -1)
            counter += 1
        elif(counter==1):
            (x2, y2) = (x, y)
            cv2.circle(img, (x,y), 2, (255,255,0), -1)
            counter += 1
        elif(counter==2):
            (x3, y3) = (x, y)
            cv2.circle(img, (x,y), 2, (255,255,0), -1)
            counter += 1
        elif(counter==3):
            (x4, y4) = (x, y)
            cv2.circle(img, (x,y), 2, (255,255,0), -1)
            counter += 1

#----------------------------

def medicion(event, x, y, flags, param):
    global x1, y1, x2, y2, drawing, mode, cal, cal_aux
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (x1, y1) = (x, y)
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            cal = cal_aux.copy()
            (x2, y2) = (x, y)
            cv2.line(cal, (x1,y1), (x2,y2), (255,0,255), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

#----------------------------

def rectificacion(image, x1, y1, x2, y2, x3, y3, x4, y4):
    # Arma los 4 puntos seleccionados de la imagen a rectificar
    srcTri = np.array( [[x1, y1],
                        [x2, y2],
                        [x3, y3],
                        [x4, y4]] ).astype(np.float32)

    # Arma las 4 esquinas de la imagen a que será rectificada
    calTri = np.array( [[0,0],
                        [image.shape[1] - 1, 0],
                        [0, image.shape[0] - 1],
                        [image.shape[1] - 1, image.shape[0] - 1]] ).astype(np.float32)

    aux = transform.rectification(image,srcTri, calTri,(image.shape[1], image.shape[0]))

    return aux


##########################################################
########################## MAIN ##########################
##########################################################

drawing  = False 
# Detecta si la imagen nueva ya fue abierta
planoCalibrado  = False
# Controla que se seleccionen 4 puntos para la rectificación
counter  = 0
# Coordenadas para la transformación afin
(x1, y1) = (0, 0)
(x2, y2) = (0, 0)
(x3, y3) = (0, 0)
(x4, y4) = (0, 0)

# Apertura de la imagen y creación de su copia
img     = cv2.imread ('imagen.jpeg', 1)
img_aux = img.copy()

# Seteo de los eventos del mouse
cv2.namedWindow('image')
cv2.setMouseCallback('image', sel_cuatro_puntos)


while(1):
    
    if(planoCalibrado == False):
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        
        # Una vez que se hayan seleccionado los 3 puntos, llama a la transformada
        if(counter==4):
            cal = rectificacion(img, x1, y1, x2, y2, x3, y3, x4, y4)
            cal_aux = cal.copy()
            
            cv2.destroyAllWindows()
            cv2.namedWindow('Plano calibrado')
            cv2.setMouseCallback('Plano calibrado', medicion)
            
            # Reinicia contador y baja las banderas
            counter   = 0
            
           ########## # Da valores para evitar que se rompa el programa si se ejecuta operación sin rectángulo dibujado
            (x1, y1) = (0, 0)
            (x2, y2) = (0, 0)
            
            # Flag que indica que ya se encuentra el plano calibrado abierto
            planoCalibrado = True
        
        if(k == 27):
            break
        
    else:
        cv2.imshow('Plano calibrado', cal)
        k = cv2.waitKey(1) & 0xFF
        
        if(k == ord('r')):
            cv2.destroyAllWindows()
            # Apertura de la imagen y creación de su copia
            img     = cv2.imread ('imagen.jpeg', 1)
            img_aux = img.copy()
            # Seteo de los eventos del mouse
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', sel_cuatro_puntos)
            planoCalibrado = False
        elif(k == 27):
            break

cv2.destroyAllWindows()


