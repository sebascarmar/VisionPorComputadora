# Ejecuté este comando: pip install --upgrade opencv-contrib-python  

import cv2
import numpy as np

print(dir(cv2.aruco))
# Cargo el diccionario predefinido
diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Creo el detector
parameters = cv2.aruco.DetectorParameters()

cap=cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()

    # Detecto los marcadores en la imagen
    corners,ids, rejected = cv2.aruco.detectMarkers(frame, diccionario, parameters=parameters)
    if(ids is not None):
        print("")
        print("esquinas: {}".format(corners))
        print("ids: {}".format(ids))
        # Dibujo los marcadores detectados en la imagen
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    cv2.imshow("ventana", frame)
    key = cv2.waitKey(50)
    if(key==27):
         break
