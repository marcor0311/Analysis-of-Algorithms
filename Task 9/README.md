[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/w_pnISvh)
# IC-3002 Tarea corta 10

Consideremos el problema del vendedor viajero.

**Problema**: Vendedor viajero.

* **Entradas**: Un grafo completo ![`G`](https://latex.codecogs.com/png.latex?G).

* **Salidas**: El camino cíclico de peso mínimo, sin elementos repetidos, que pase por cada uno de los vértices de ![`G`](https://latex.codecogs.com/png.latex?G).

Debemos resolver este problema utilizando algoritmos genéticos. Las soluciones al problema se modelan como listas de vértices, cada vértice representado como un número natural, de acuerdo a la estrategia planteada en la lectura de algoritmos probabilísticos. 

La clase de `dominio_tsp.DominioTSP` representa el dominio de soluciones al problema del vendedor viajero (TSP). Esta clase se utilizará en el algoritmo genético. 

Implemente la siguientes funciones:

1. En el archivo `dominio_tsp.py`: `fcosto`, `cruzar`, `mutar`
2. En el archivo `algoritmo_genetico.py`: `optimizar`

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

### Diseño del algoritmo (5 pts)

* (5 pts) El código implementa un algoritmo genético.
* (0 pts) El código no implementa un algoritmo genético.
