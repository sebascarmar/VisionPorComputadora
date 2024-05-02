# El programa debe permitir dibujar un rectángulo en la imagen. Luego, al presionar:
#   'g'  : debe guardar el recorte de imagen seleccionado.
#   'r'  : debe eliminar la selección y permitir volver a seleccionar.
#   'esc': debe salir del programa


import cv2
import numpy as np


######################## FUNCIONES #######################

def select_image(event, x, y, flags, param):
    global xi, yi, x1, y1, x2, y2, x3, y3, drawing, mode, img, counter

    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing  = True
        (xi, yi) = (x, y)
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing is True):
            #img = img_aux.copy()
            if(counter==0):
                (x1, y1) = (x, y)
                cv2.circle(img, (x,y), 5, (255,0,255), -1)
                counter += 1
            elif(counter==1):
                (x2, y2) = (x, y)
                cv2.circle(img, (x,y), 5, (255,0,255), -1)
                counter += 1
            elif(counter==2):
                (x3, y3) = (x, y)
                cv2.circle(img, (x,y), 5, (255,0,255), -1)
                counter += 1
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if(counter==0):
            (x1, y1) = (x, y)
            cv2.circle(img, (x,y), 5, (255,0,255), -1)
            counter += 1
        elif(counter==1):
            (x2, y2) = (x, y)
            cv2.circle(img, (x,y), 5, (255,0,255), -1)
            counter += 1
        elif(counter==2):
            (x3, y3) = (x, y)
            cv2.circle(img, (x,y), 5, (255,0,255), -1)
            counter += 1


########################## MAIN ##########################

drawing  = False 
mode     = True 
counter  = 0
(xi, yi) = (-1, -1)
(x1, y1) = (-1, -1)
(x2, y2) = (-1, -1)
(x3, y3) = (-1, -1)

img     = cv2.imread ('perros.jpeg', 0)
img_aux = img.copy()
img2    = cv2.imread ('mujer_tapando.jpeg', 0)

cv2.namedWindow('image')
cv2.setMouseCallback('image', select_image)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF

    if(k == ord('r')):
        img = img_aux.copy()
    #elif(k == ord('a')):
        #cv2.imwrite('resultado.png', img_aux[yi:yf,xi:xf])
    elif(k == 27):
        break

    if(counter==3):
        x4=(x2-x1)+x3
        y4=(y2-y1)+y3

        srcTri = np.array( [[0,0],
                            [img2.shape[1] - 1, 0],
                            [0, img2.shape[0] - 1]] ).astype(np.float32)
        dstTri = np.array( [[x1, y1],
                            [x2, y2],
                            [x3, y3],
                            [x4, y4]] ).astype(np.float32)
        
        M = cv2.getAffineTransform(srcTri, dstTri[:3])
        
        transformed_img = cv2.warpAffine(img2, M, (img.shape[1], img.shape[0]))


        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [dstTri[:3].astype(int)], (255,255,255))
        cv2.fillPoly(mask, [dstTri[1:].astype(int)], (255,255,255))
        
        # Crear una imagen combinada del mismo tamaño que la imagen original
        img_combinada = np.zeros_like(img, dtype=np.uint8)
        # Aplicar la máscara para combinar las dos imágenes
        for c in range(img.shape[2]):
            img_combinada[:,:,c] = np.where(mask == 0, img[:,:,c], transformed_img[:,:,c])

        #img_combinada[:] = np.where(mask == 0, img[:], transformed_img[:])

       ## Calcula la imagen mezclada con la imagen original
       # img_with_transformed = cv2.addWeighted(img, 1, transformed_img, 0.9, 0)
       # # Máscara inversa
       # mask_inv = cv2.bitwise_not(mask)
       # # Combinar la imagen original con la imagen transformada usando la máscara
       # img = cv2.bitwise_and(img_with_transformed, img_with_transformed, mask=mask_inv)
       # img = cv2.add(img, transformed_img)
        img[:]= img_combinada
        cv2.imwrite('resultado.png', img_combinada)
        counter += 1

cv2.destroyAllWindows()




