# Propiedades de vídeo

Este programa tiene la flexibilidad de tomar el valor de _frames por segundo_ correspondientes al vídeo que se le da 
como entrada. Esto permite que no se _hardcodee_ el **delay** del **waitKey**. Además, también detecta el ancho y el
alto del vídeo para dimensionarlo cuando se lo guarde en el archivo de salida, por lo que no se _harcodea_ el **frameSize**.

Para ejecutar el programa se debe escribir el siguiente comando:

```bash
> python3.8 tp3.py videoIn.mp4
```
