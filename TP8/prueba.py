import cv2
import numpy as np

# Leer la imagen
img     = cv2.imread('cancha.png', 1)

# Definir los puntos de origen y destino
origen = np.array([[64,234], [482,3], [452,478], [790,90]]).astype(np.float32)
destino = np.array([[0,0], [1000,0], [0,500], [500,1000]]).astype(np.float32)

# Calcular la matriz de transformación
M = cv2.getPerspectiveTransform(origen, destino)

# Aplicar la transformación a la imagen
img_rectificada = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

# Mostrar la imagen rectificada
cv2.imshow('Imagen Rectificada', img_rectificada)
cv2.waitKey(0)
cv2.destroyAllWindows()

