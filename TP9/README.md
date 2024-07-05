# Medición de objetos sobre plano calibrado

Este programa utiliza una imagen en perspectiva. Esta imagen es de una mesa que contiene en su centro
una parte de acrílico. Este acrílico es el plano que se calibra para poder realizar mediciones de 
longitud, para lo cual se encuentran distintos objetos: regla de 30cm, tarjeta Red Bus, hoja A4,
placa virgen de cobre.

> **Medida de los objetos:**
> - 41x93.5 cm  -> acrílico de la mesa
> - 15x15   cm  -> placa
> - 21x29.7 cm  -> hoja
> - 31.5x3  cm  -> regla
> - 8.6x5.4 cm  -> tarjeta


El programa consta de 3 partes: rectifcación, calibración y medición.

**1. Rectificación**: se seleccionan las 4 esquinas del acrílico en el siguiente orden:
  1. la más cercana a la regla
  2. la más cercana a la placa de cobre
  3. la más cerca a la tarjeta
  4. la más cerca a la hoja A4 (si el monitor no permite verla, hacer zoom con el scroll y las flechas de la ventana para desplazarse)

**2. Calibración**: ahora se utilizan las dimensiones de la placa de cobre para poder
modificar la relación de aspecto del plano, y que así sea representativo de la realidad:
  1. se marcan los extremos que forman el borde horizontal de la placa
  2. se marcan los extremos que forman el borde vertical de la placa

**3. Medición**: seleccionar los 2 puntos del segmento que se desee medir. **El valor de medición aparecerá sobre el primer punto marcado**.
  - 'r' : presionando esta tecla se limpian las mediciones sobre el plano y se puede seguir midiendo.


El programa se ejecuta con el siguiente comando:

```bash
> python3.8 tp9.py
```



