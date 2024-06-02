# El programa rectifica una imagen, la calibra con dos longitudes conocidas,
#y permite medir. Se tienen las siguientes opciones:
#   'r'  : permite limpiar el plano y seguir midiendo
#   'esc': debe salir del programa

# Medidas de objetos:
#   41x93.5 cm  -> acrílico de la mesa
#   15x15   cm  -> placa
#   21x29.7 cm  -> hoja
#   31.5x3  cm  -> regla
#   8.6x5.4 cm  -> tarjeta

import cv2
import numpy as np
import transform
import math


######################## funciones #######################

def sel_cuatro_puntos(event, x, y, flags, param):
    global x1, y1, x2, y2, x3, y3, x4, y4
    global img, counter 

    if event == cv2.EVENT_LBUTTONUP:
        if(counter==0):
            (x1, y1) = (x, y)
            cv2.circle(img, (x,y), 4, (255,255,0), -1)
            counter += 1
        elif(counter==1):
            (x2, y2) = (x, y)
            cv2.circle(img, (x,y), 4, (255,255,0), -1)
            counter += 1
        elif(counter==2):
            (x3, y3) = (x, y)
            cv2.circle(img, (x,y), 4, (255,255,0), -1)
            counter += 1
        elif(counter==3):
            (x4, y4) = (x, y)
            cv2.circle(img, (x,y), 4, (255,255,0), -1)
            counter += 1

#----------------------------

def calibracion(event, x, y, flags, param):
    global x1, y1, x2, y2, primerPto, segundoPto, rec, rec_aux
    global counter, longConocidaA_pix, longConocidaB_pix

    if(event == cv2.EVENT_LBUTTONDOWN and primerPto == False):
        primerPto  = True
        (x1, y1) = (x, y)
        cv2.circle(rec, (x1,y1), 4, (255,0,255), -1)
    elif(event == cv2.EVENT_LBUTTONDOWN and segundoPto == False):
        segundoPto = True
        (x2, y2) = (x, y)
        cv2.circle(rec, (x2,y2), 4, (255,0,255), -1)
    elif(event == cv2.EVENT_LBUTTONUP and primerPto == True and segundoPto == True):
        if(counter == 0):
            longConocidaA_pix = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
            counter += 1
        else:
            longConocidaB_pix = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
            counter += 1
        
        rec = rec_aux.copy()
        cv2.line(rec, (x1,y1), (x2,y2), (255,0,255), 2)
        
        primerPto  = False
        segundoPto = False

#----------------------------

def medicion(event, x, y, flags, param):
    global x1, y1, x2, y2, primerPto, segundoPto, cal, cal_aux
    global  longAMedirA_pix, longAMedirB_pix, pixCm_Y # Puede ser también pixCm_X
    
    if(event == cv2.EVENT_LBUTTONDOWN and primerPto == False):
        primerPto  = True
        (x1, y1) = (x, y)
        cv2.circle(cal, (x1,y1), 4, (0,255,255), -1)
    elif(event == cv2.EVENT_LBUTTONDOWN and segundoPto == False):
        segundoPto  = True
        (x2, y2) = (x, y)
        cv2.circle(cal, (x2,y2), 4, (0,255,255), -1)
    elif(event == cv2.EVENT_LBUTTONUP and primerPto == True and segundoPto == True):
        cv2.line(cal, (x1,y1), (x2,y2), (0,255,255), 2)
        longAMedirA_pix = x2-x1 if(x2>x1) else x1-x2
        longAMedirB_pix = y2-y1 if(y2>y1) else y1-y2
        longMedidaPix = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
        longMedidaCm  = longMedidaPix/pixCm_Y
        
        cv2.putText(cal, str(round(longMedidaCm,2))+"cm", (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
        
        primerPto  = False
        segundoPto = False

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
# Banderas
primerPto  = False 
segundoPto = False 
planoRectificado = False
planoCalibrado   = False
# Control de selección de puntos en rectificación y calibración
counter  = 0
# Coordenadas para la rectificación, calibración y medición
(x1, y1) = (0, 0)
(x2, y2) = (0, 0)
(x3, y3) = (0, 0)
(x4, y4) = (0, 0)
# Longitudes medidas en pixeles
longConocidaA_cm = 15.0
longConocidaB_cm = 15.0
longConocidaA_pix = 0
longConocidaB_pix = 0
longAMedirA_pix   = 0
longAMedirB_pix   = 0

# Apertura de la imagen y creación de su copia
img     = cv2.imread ('imagen.jpeg', 1)
img     = cv2.resize(img, (int(img.shape[1]/2.2), int(img.shape[0]/2.2)))
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
            
            # Reinicia contador
            counter   = 0
            
            # Flag que indica que ya se hizo la rectificación
            planoRectificado = True
         
        elif(k == 27):
            break
        
    elif(planoCalibrado == False):
        cv2.imshow('Plano rectificado - Realice calibracion', rec)
        k = cv2.waitKey(1) & 0xFF
        
        if(counter==2):
            # Se calculan las relaciones pixel/cm, y el objetivo es que sean iguales
            pixCm_Y = longConocidaB_pix/longConocidaB_cm
            pixCm_X = longConocidaA_pix/longConocidaA_cm
            # Para eso se busca un factor de correción
            k = pixCm_Y/pixCm_X
            # Aquí se aplica la correción
            if(k>1):
                cal = cv2.resize(rec_aux, (int(k*rec_aux.shape[1]),rec_aux.shape[0]))
            else:
                cal = cv2.resize(rec_aux, (rec_aux.shape[1],int(k*rec_aux.shape[0])))
            
            cal_aux = cal.copy()
            
            cv2.destroyAllWindows()
            cv2.namedWindow('Plano calibrado')
            cv2.setMouseCallback('Plano calibrado', medicion)
            
            # Flag que indica que ya se encuentra el plano calibrado 
            planoCalibrado = True
         
        elif(k == ord('r')):
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


