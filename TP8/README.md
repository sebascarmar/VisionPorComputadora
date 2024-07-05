# Rectificación de imágenes

Este programa utiliza la misma imagen del tp2 (hoja), mostrándola en una ventana. En esa ventana se
pueden realizar las siguientes acciones la presionar determiandas teclas:

- 'g'  : guarda el recorte de imagen seleccionado.

- 'e'  : aplica una transformación euclidiana al recorte seleccionado. Para ello traslada **100** pixeles
en _x_ y en _y_, y rota **45º** (estos valores pueden ser cambiados en el código).

- 's'  : aplica una transformación similaridad al recorte seleccionado, escalando por **0.5** (este valor
puede ser cambiado en el código).

- 'a'  : cambia la imagen de fondo y abre una de la **Bombonera**. Luego, se seleccionan 3 puntos y
allí se incrusta la imagen del **escudo de boca** (la transformación afín es aplicada a la imagen del 
escudo de Boca).

- 'h'  : cambia la imagen que se muestra en la ventana, y abre la de una **cancha de fútbol** en perspectiva.
El roden de elección de los 4 puntos debe ser: equinas sup. izq., sup. der., inf. izq e inf. der.

- 'p'  : vuelve a abrir la imagen de la hoja, ya sea después de incrustar la imagen del escudo de Boca en 
la Bombonera, como también luego de rectificar la imagen de la cancha.

- 'r'  : elimina la selección y permite volver a seleccionar, ya sea en la imagen de la hoja, la del
estadio o en la de la cancha rectificada (luego de realizar la incrustación de imágenes o luego de rectificar).

- 'esc': sale del programa.


El programa se ejecuta con el siguiente comando:

```bash
> python3.8 tp8.py
```



