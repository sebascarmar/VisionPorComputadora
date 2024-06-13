import cv2
import numpy as np

# Cargo el diccionario predefinido
diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Genero el marcador
imagen = np.zeros((200,200), dtype=np.uint8)
cv2.aruco.generateImageMarker(diccionario, 33, 200, imagen, 1)


cv2.imwrite("marker33.png", imagen)
cv2.imshow("ventana", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
