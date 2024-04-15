#!/usr/bin/env python3
#-*-coding:utf-8-*-

import cv2

img = cv2.imread ('../TP2/hoja.png', 0)

cv2.imshow ('Imagen', img)

k = cv2.waitKey(0)
if k == ord ( 'g' ) : #si se presiona la letra ’g’ se guarda la imagen
    print('Guardando imagen en escala de grises.')
    cv2.imwrite('imagen_gris.png', img)
else :
    print('Imagen no guardada.')

cv2.destroyAllWindows()
