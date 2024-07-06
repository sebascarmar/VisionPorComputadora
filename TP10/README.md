# ArUCo

## 1. Control del camino de un robot móvil

Este programa permite dibujar el camino del robot (que posee un marcador ArUCo). Este camino
es dibujado en la imagen tomada por la cámara de vídeo que capta al robot. En esta ventana
se pueden realizar las siguientes acciones:

- 'd' : dibuja/no-dibuja el camino del robot.

- 'r' : limpia la pantalla.

- 'esc': sale del programa.

El programa se ejecuta con el siguiente comando:
``` bash
> python3.8 tp10.1.py
```

> **NOTA**: teniendo los datos de un entorno fijo por el cual se moverá el robot, se puede tomar
>un sistema de referencia _World_, y de esta forma puede obtenerse la pose del robot $(x_0,y_0,\theta)$,
>pudiendo así realimentar al robot para controlarlo.


## 2. Medición de longitudes en un plano en perspectiva

La idea surge por la consigna del TP9, pero pudiendo realizar mediciones sin necesidad de rectificar
el plano. Es decir, se puede medir estando aún en perspectiva. Al iniciar el programa automáticamente 
se pueden marcar los extremos que forman la longitud que se desea medir.

El programa se ejecuta con el siguiente comando:
``` bash
> python3.8 tp10.2.py
```
