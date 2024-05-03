# el programa debe permitir dibujar un rectángulo en la imagen. luego, al presionar:
#   'g'  : debe guardar el recorte de imagen seleccionado.
#   'e'  : aplica una transformación euclidiana al recorte seleccionado.
#   's'  : aplica una transformación similaridad al recorte seleccionado.
#   'a'  : aplica una transformación afin, e incrusta imagen en selección de 3 puntos.
#   'r'  : debe eliminar la selección y permitir volver a seleccionar.
#   'p'  : vuelve a mostrar la primer imagen abierta (la hoja en este caso).
#   'esc': debe salir del programa.


import cv2
import numpy as np
import transform


######################## funciones #######################

def select_image(event, x, y, flags, param):
    global xi, yi, xf, yf, x1, y1, x2, y2, x3, y3, x4, y4
    global drawing, mode, img, counter, afin_mode

    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (xi, yi) = (x, y)

    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            if( afin_mode is True):
                if(counter==0):
                    (x1, y1) = (x, y)
                    cv2.circle(img, (x,y), 2, (255,0,255), -1)
                elif(counter==1):
                    (x2, y2) = (x, y)
                    cv2.circle(img, (x,y), 2, (255,0,255), -1)
                elif(counter==2):
                    (x3, y3) = (x, y)
                    cv2.circle(img, (x,y), 2, (255,0,255), -1)
             
            elif( rectification_mode is True):
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
             
            else:
                img = img_aux.copy()
                (xf, yf) = (x, y)
                cv2.rectangle(img, (xi,yi), (x,y), (0,0,0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if( afin_mode is True):
            if(counter==0):
                (x1, y1) = (x, y)
                cv2.circle(img, (x,y), 2, (255,0,255), -1)
                counter += 1
            elif(counter==1):
                (x2, y2) = (x, y)
                cv2.circle(img, (x,y), 2, (255,0,255), -1)
                counter += 1
            elif(counter==2):
                (x3, y3) = (x, y)
                cv2.circle(img, (x,y), 2, (255,0,255), -1)
                counter += 1
                
        elif(rectification_mode is True):
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
         
        else:
            cv2.rectangle(img, (xi,yi), (x,y), (0,0,0), 2)

#----------------------------

def euclidiana(image, angle, tx, ty):
    aux          = transform.translate(image, x=tx, y=ty)
    tras_and_rot = transform.rotate(aux, angle, center=None, scale=1.0)

    return tras_and_rot
    
#----------------------------

def similaridad(image, angle, tx, ty, s):
    aux                = transform.translate(image, x=tx, y=ty)
    tras_rot_and_scale = transform.rotate(aux, angle, center=None, scale=s)

    return tras_rot_and_scale

#----------------------------

def img_inside_img(dstTri, image1, image2):
    # Cálculo del 4 punto del palalegramo
    x4=(dstTri[1][0]-dstTri[0][0])+ dstTri[2][0] #(x2-x1)+x3
    y4=(dstTri[1][1]-dstTri[0][1])+ dstTri[2][1] #(y2-y1)+y3
    dstTri = np.append(dstTri, [[x4,y4]],axis=0).astype(np.float32)
    # Crea una imagen en negro del mismo tamaño que la imagen1
    mask = np.zeros(image1.shape[:2], dtype=np.uint8)
    # Genera la máscara mediante dos triángulos
    cv2.fillPoly(mask, [dstTri[:3].astype(int)], (255,255,255))
    cv2.fillPoly(mask, [dstTri[1:].astype(int)], (255,255,255))
    
    # Crear una imagen combinada del mismo tamaño que la imagen1
    combination = np.zeros_like(image1, dtype=np.uint8)
    # Aplicar la máscara para combinar las dos imágenes (cond ? t : f)
    for c in range(image1.shape[2]):
        combination[:,:,c] = np.where(mask == 0, image1[:,:,c], image2[:,:,c])
    # En caso de que las imágenes sean a blanco y negro
    #combination[:] = np.where(mask == 0, img[:], transformed_img[:])

    return combination

#----------------------------

def afin_y_combinacion(image2, x1, y1, x2, y2, x3, y3, image1):
    # Arma las 3 esquinas de la imagen a transformar
    srcTri = np.array( [[0,0],
                        [image2.shape[1] - 1, 0],
                        [0, image2.shape[0] - 1]] ).astype(np.float32)
    # Arma los 3 puntos seleccionados hacia donde se transformará la imagen
    dstTri = np.array( [[x1, y1],
                        [x2, y2],
                        [x3, y3]] ).astype(np.float32)

    aux = transform.afin(image2,srcTri, dstTri,(image1.shape[1], image1.shape[0]))
    cv2.imwrite('afin.png', aux)

    combination = img_inside_img(dstTri, image1, aux)

    return combination

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

    return aux

########################## MAIN ##########################

drawing  = False 
# Coordenadas para dibujar rectángulo
(xi, yi) = (0, 0)
(xf, yf) = (1, 1)
# Bandera que indica si se está en modo afin, ya que cambia el dibujo
afin_mode= False 
# Detecta si la imagen nueva ya fue abierta
new_img  = False
# Controla que se seleccionen 3 puntos antes transformar afín
counter  = 0
# Coordenadas para la transformación afin
(x1, y1) = (0, 0)
(x2, y2) = (0, 0)
(x3, y3) = (0, 0)
(x4, y4) = (0, 0)

rectification_mode = False 

# Parámetros de transformación
angle  = 45
tras_x = 100
tras_y = 100
scale  = 0.5

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

    elif(k == ord('s')): # transformación similaridad
        dst = similaridad(img_aux[yi:yf,xi:xf], angle, tras_x, tras_y, scale)
        cv2.imwrite('similaridad.png', dst)

    elif(k == ord('a') or afin_mode): # transformación afín
        # Controla que se ejecute una sola vez
        if(new_img == False):
            afin_mode = True
            img     = cv2.imread('bombonera.png', 1)
            img_aux = img.copy()
            img2    = cv2.imread('escudo.png', 1)
            new_img = True
        
        # Una vez que se hayan seleccionado los 3 puntos, llama a la transformada
        if(counter==3):
            dst = afin_y_combinacion(img2, x1, y1, x2, y2, x3, y3, img)
            
            cv2.imwrite('combinacion.png', dst)
            img[:]     = dst
            img_aux[:] = dst
            
            # Reinicia contador y baja las banderas
            counter   = 0
            afin_mode = False
            new_img   = False
            
            # Da valores para evitar que se rompa el programa si se ejecuta operación sin rectángulo dibujado
            (xi, yi) = (0, 0)
            (xf, yf) = (1, 1)

    elif(k == ord('h') or rectification_mode): # rectificación
        # Controla que se ejecute una sola vez
        if(new_img == False):
            rectification_mode = True
            img     = cv2.imread('cancha.png', 1)
            img_aux = img.copy()
            new_img = True
        
        # Una vez que se hayan seleccionado los 3 puntos, llama a la transformada
        if(counter==4):
            dst = rectificacion(img, x1, y1, x2, y2, x3, y3, x4, y4)
            
            cv2.imwrite('rectificacion.png', dst)
            img[:]     = dst
            img_aux[:] = dst
            
            # Reinicia contador y baja las banderas
            counter   = 0
            rectification_mode = False
            new_img   = False
            
            # Da valores para evitar que se rompa el programa si se ejecuta operación sin rectángulo dibujado
            (xi, yi) = (0, 0)
            (xf, yf) = (1, 1)

    elif(k == ord('p')): # abre la imagen de la hoja
        img     = cv2.imread ('../TP2/hoja.png', 1)
        img_aux = img.copy()

    elif(k == 27):
        break

cv2.destroyAllWindows()


