# Ejecuté este comando: pip install --upgrade opencv-contrib-python  

# El programa detecta el marcador 33 de Aruco, y a partir de su centro
#puede dibujar en base a su movimiento. La aplicación es para controlar
#el camino de un robot mediante una cámara. Con:
#   'd'  : permite que se dibuje o se deje de dibujar.
#   'r'  : limpia la pantalla de cualquier dibujo.
#   'esc': sale del programa

import cv2
import numpy as np

# Carga el diccionario predefinido
diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Crea el detector
parameters = cv2.aruco.DetectorParameters()

# Lista para almacenar las posiciones del centro del identificador
posiciones_centro_id = []

# Bandera que permite dibujar en pantalla o no
dibujar = False

cap=cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()

    # Detecta el marcadores en la imagen
    corners,ids,rejected = cv2.aruco.detectMarkers(frame, diccionario, parameters=parameters)
    if(ids == 33):
        # Dibuja el marcador detectado en la imagen
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Calcula el centro del Aruco
        x0 = corners[0][0][0][0]
        x1 = corners[0][0][1][0]
        x2 = corners[0][0][2][0]
        x3 = corners[0][0][3][0]
        centro_x = int((x0+x1+x2+x3)/4)
        
        y0 = corners[0][0][0][1]
        y1 = corners[0][0][1][1]
        y2 = corners[0][0][2][1]
        y3 = corners[0][0][3][1]
        centro_y = int((y0+y1+y2+y3)/4)
        
        # Almacena el centro del id
        if dibujar:
            posiciones_centro_id.append((centro_x,centro_y))
#        # Dibuja los marcadores detectados en la imagen
#        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.putText(frame, f"({centro_x}px,{centro_y}px)", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Dibuja las posiciones almacenadas, reflejando un dibujo continuo
    for i in range(1, len(posiciones_centro_id)):
        cv2.line(frame, posiciones_centro_id[i-1], posiciones_centro_id[i], (255, 0, 255), 2)


    cv2.imshow("ventana", frame)

    key = cv2.waitKey(50)

    if(key == ord('d')):     # Togglea entre dibujar y no dibujar
        dibujar = not dibujar
    elif(key == ord('r')):   # Limpia la pantalla
        posiciones_centro_id.clear()
    elif(key==27):           # Sale del bucle
         break


