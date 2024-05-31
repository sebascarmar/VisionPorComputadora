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
#21.cmx29.7cm  -> hoja

import cv2
import numpy as np
import transform
import math


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

def calibracion(event, x, y, flags, param):
    global x1, y1, x2, y2, drawing, rec, rec_aux
    global counter2, longConocidaA, longConocidaB

    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (x1, y1) = (x, y)
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            rec = rec_aux.copy()
            (x2, y2) = (x, y)
            cv2.line(rec, (x1,y1), (x2,y2), (255,0,255), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        if(counter2 <= 0):
            #longConocidaA = x2-x1 if(x2>x1) else x1-x2
            longConocidaA = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
            counter2 += 1
        else:
            longConocidaB = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
            counter2 += 1
        
        drawing = False

#----------------------------

def medicion(event, x, y, flags, param):
    global x1, y1, x2, y2, drawing, cal, cal_aux
    global  longAMedirA, longAMedirB, pixCm_Y
    
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (x1, y1) = (x, y)
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            cal = cal_aux.copy()
            (x2, y2) = (x, y)
            cv2.line(cal, (x1,y1), (x2,y2), (0,255,255), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        longAMedirA = x2-x1 if(x2>x1) else x1-x2
        longAMedirB = y2-y1 if(y2>y1) else y1-y2
        longMedidaPix = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
        longMedidaCm  = longMedidaPix/pixCm_Y
        
        cv2.putText(cal, str(round(longMedidaCm,2))+"cm", (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
        
        drawing = False

#----------------------------

def rectificacion(image, x1, y1, x2, y2, x3, y3, x4, y4):
    # Arma los 4 puntos seleccionados de la imagen a rectificar
    srcTri = np.array( [[x1, y1],
                        [x2, y2],
                        [x3, y3],
                        [x4, y4]] ).astype(np.float32)

    # Arma las 4 esquinas de la imagen a que será rectificada
    dstTri = np.array( [[0,0],
                        [image.shape[1] - 1, 0],
                        [0, image.shape[0] - 1],
                        [image.shape[1] - 1, image.shape[0] - 1]] ).astype(np.float32)

    aux = transform.rectification(image,srcTri, dstTri,(image.shape[1], image.shape[0]))

    # Ajusta la imagen a un tamaño fijo siempre. Luego se corrige el ratio en la calibración
    aux = cv2.resize(aux, (800, 410))
    #cv2.imwrite('planoCalibrado.png', imagen_redimensionada)

    return aux


##########################################################
########################## MAIN ##########################
##########################################################

drawing  = False 
# Detecta si la imagen nueva ya fue abierta
planoRectificado = False
planoCalibrado   = False
# Controla que se seleccionen 4 puntos para la rectificación
counter  = 0
counter2  = 0
# Coordenadas para la transformación afin
(x1, y1) = (0, 0)
(x2, y2) = (0, 0)
(x3, y3) = (0, 0)
(x4, y4) = (0, 0)
# Longitudes medidas en pixeles
longConocidaA = 0
longConocidaB = 0
longAMedirA   = 0
longAMedirB   = 0
# Medidas conocidas de algún objeto
#alto  = 
#ancho

# Apertura de la imagen y creación de su copia
img     = cv2.imread ('imagen.jpeg', 1)
img     = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
img_aux = img.copy()

# Seteo de los eventos del mouse
cv2.namedWindow('image')
cv2.setMouseCallback('image', sel_cuatro_puntos)


while(1):
    
    if(planoRectificado == False):
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        
        # Una vez que se hayan seleccionado los 3 puntos, llama a la transformada
        if(counter==4):
            rec = rectificacion(img_aux, x1, y1, x2, y2, x3, y3, x4, y4)
            rec_aux = rec.copy()
            
            cv2.destroyAllWindows()
            cv2.namedWindow('Plano rectificado - Realice calibracion')
            cv2.setMouseCallback('Plano rectificado - Realice calibracion', calibracion)
            
            # Reinicia contador y baja las banderas
            counter   = 0
            
           ########## # Da valores para evitar que se rompa el programa si se ejecuta operación sin rectángulo dibujado
            (x1, y1) = (0, 0)
            (x2, y2) = (0, 0)
            
            # Flag que indica que ya se encuentra el plano calibrado abierto
            planoRectificado = True
        
        if(k == 27):
            break
        
    elif(planoCalibrado == False):
        cv2.imshow('Plano rectificado - Realice calibracion', rec)
        k = cv2.waitKey(1) & 0xFF
        
        if(counter2==2):
            # Se calculan las relaciones pixel/cm, y el objetivo es que sean iguales
            pixCm_Y = longConocidaB/15
            pixCm_X = longConocidaA/15
            # Para eso se busca un factor de correción
            k = pixCm_Y/pixCm_X
            # Aquí se aplica la correción
            if(k>1):
                cal = cv2.resize(rec_aux, (int(k*rec_aux.shape[1]),rec_aux.shape[0]))
            else:
                cal = cv2.resize(rec_aux, (rec_aux.shape[1],int(k*rec_aux.shape[0])))

            cal_aux = cal.copy()
            #imagen_redimensionada = cv2.resize(aux, (935, 410))
            #cv2.imwrite('planoCalibrado.png', imagen_redimensionada)
            
            cv2.destroyAllWindows()
            cv2.namedWindow('Plano calibrado')
            cv2.setMouseCallback('Plano calibrado', medicion)
            
            # Reinicia contador y baja las banderas
            counter  = 0
         
            # Flag que indica que ya se encuentra el plano calibrado abierto
            planoCalibrado = True

        if(k == ord('r')):
            cv2.destroyAllWindows()
            # Apertura de la imagen y creación de su copia
            img     = cv2.imread ('imagen.jpeg', 1)
            img     = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
            img_aux = img.copy()
            # Seteo de los eventos del mouse
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', sel_cuatro_puntos)
            planoRectificado = False
            planoCalibrado   = False
            
        elif(k == 27):
            break
        
    else:
        cv2.imshow('Plano calibrado', cal)
        k = cv2.waitKey(1) & 0xFF

        if(k == ord('r')):
           cal = cal_aux.copy()
        elif(k == 27):
            break


cv2.destroyAllWindows()


