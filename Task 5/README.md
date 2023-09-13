[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/Ge12nUeP)
# IC-3002 Tarea corta 6

Considere el siguiente problema computacional:

**Problema**: Ordenar una secuencia de números enteros.
* **Entradas**: ![](https://latex.codecogs.com/png.latex?%28A%2Cn%29) tal que ![](https://latex.codecogs.com/png.latex?%20A%20%3D%20%28a_1%2C%20a_2%2C%20%5Cdots%2C%20a_n%7Ca_k%20%5Cin%20%5Cmathbb%7BZ%7D%29%20%5Cland%20n%20%3D%20%7CA%7C)
* **Salidas**: La secuencia ![](https://latex.codecogs.com/png.latex?A) ordenada de manera tal que ![](https://latex.codecogs.com/png.latex?%5Cunderset%7B0%20%5Cleq%20i%20%3C%20j%20%3C%20n%7D%20%7B%5Cforall%20i%2C%20j%7D%20%3A%20a_i%20%5Cleq%20a_j)


Este problema se puede resolver, entre otras opciones, con el algoritmo de ordenamiento *quicksort*. 

1. Implemente en el archivo `quicksort.py` la función `quicksort` para realizar ordenamiento *quicksort* sobre una lista de enteros.

2. Implemente en el archivo `quicksort_test.py` las funciones `generar_peor_caso(n)` y `generar_caso_promedio(n)` para generar correspondientemente listas de enteros de tamaño `n` que provoquen los casos peor y promedio para `quicksort`.

3. Implemente en el archivo `quicksort.py` la función `quicksort_mejorado` como una mejora a la función `quicksort` de manera tal que el algoritmo se comporte con el caso promedio incluso cuando lo probamos con listas producidas por `generar_peor_caso`.


## Cómo instalar el ambiente de desarrollo y ejecutar las pruebas localmente

Este proyecto requiere `python3`. Asegúrese que esté instalado en su distribución de linux.

Si no lo ha hecho anteriormente, crear un ambiente virtual para las dependencias

```bash
python3 -m venv .venv
```

Activar el ambiente virtual

```bash
source .venv/bin/activate
```

Instalar las dependencias

```bash
pip3 install -r requirements.txt
```

Ejecutar las pruebas

```bash
pytest -s -W ignore::DeprecationWarning
```

## Rúbrica

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con los requerimientos solicitados.
* (3 pts) La producción cumple parcialmente con los requerimientos solicitados.
* (1 pts) La producción, en su mayor parte, no cumple con los requerimientos solicitados.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa la mayoría de las pruebas automatizadas.

### Mejoras (5 pts)

* (5 pts) El código mejorado cumple con el requerimiento solicitado.
* (1 pts) El código mejorado no cumple con el requerimiento solicitado.
