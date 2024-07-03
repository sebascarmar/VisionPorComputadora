# Ejecuté este comando: pip install --upgrade opencv-contrib-python  

# El programa permite medir longitudes pertenecientes al mismo plano
#del marcador Aruco. Se debe utilizar el marcador 33 y debe tener
#una longitud real de 70x70mm. Con:
#   'esc': debe salir del programa

import cv2
import numpy as np


# Lista que tendrá los dos puntos marcados por el usuario para medir longitudes.
points = []

######################################################################################
def marca_puntos(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) > 2:
            points.pop(0)


######################################## MAIN ########################################

# Tamaño e ID del aruco
size_aruco = 70  # mm
id_aruco   = 33

# Carga el diccionario predefinido
diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Crea el detector
parameters = cv2.aruco.DetectorParameters()

# Arma las 4 esquinas de la imagen a donde se rectificará en un cuadrado
#de 70x70 pix. De esta forma garantiza la relación pix/mm=1
dst_corners = np.array( [[0           ,           0],
                         [size_aruco-1,           0],
                         [size_aruco-1,size_aruco-1],
                         [0           ,size_aruco-1]] ).astype(np.float32)

# Abre la cámara y setea la función de callback
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', marca_puntos)


while True:
    ret, frame = cap.read()

    # Detectar los marcadores ArUco en la imagen
    corners,ids,rejected = cv2.aruco.detectMarkers(frame, diccionario, parameters=parameters)

    # Si detecta el aruco de ID=33
    if (ids == id_aruco):
        # Dibuja el marcador detectado en la imagen
        frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Obtiene las esquinas del aruco detectado
        src_corners = np.array( [corners[0][0][0],
                                 corners[0][0][1],
                                 corners[0][0][2],
                                 corners[0][0][3]] ).astype(np.float32)
        
        # Obtiene la matriz de transformación de perspectiva M
        M = cv2.getPerspectiveTransform(src_corners, dst_corners)
        
        # Solo si hay dos puntos seleccionados (solo evita funcionar en el inicio del programa)
        if len(points) == 2:
            # Dibuja los círculo y el segmento a medir
            cv2.circle(frame, points[0], 5, (0, 0, 255), -1)
            cv2.circle(frame, points[1], 5, (0, 0, 255), -1)
            cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
           
            # Transforma los puntos con el uso de la matriz M
            p1 = np.array([[points[0][0]],
                           [points[0][1]],
                           [           1]])
            p2 = np.array([[points[1][0]],
                           [points[1][1]],
                           [        1   ]])
            
            p1_rect = np.dot(M,p1)
            p1_rect = p1_rect / p1_rect[2] # normaliza
            
            p2_rect = np.dot(M,p2)
            p2_rect = p2_rect / p2_rect[2] # normaliza
            
            # Calcula la distancia, sabiendo que la relación pix/mm = 1
            longitud = np.sqrt((p2_rect[0]-p1_rect[0])**2 + (p2_rect[1]-p1_rect[1])**2)
            cv2.putText(frame, f"Longitud: {longitud[0]:.2f} mm", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)



    cv2.imshow('frame', frame)

    key = cv2.waitKey(50) & 0xFF
    if(key==27):
         break


cap.release()
cv2.destroyAllWindows()

