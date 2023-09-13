from typing import List
import random
from dominio_tsp import DominioTSP

def optimizar(dominio: DominioTSP, tam_pobl: int, porc_elite: float, prob_mut: float, reps: int) -> List[int]:
    """
    Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    tam_pobl (int)
        Tamaño de la población.
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
    (List[int]) Estructura de datos según el dominio, que representa una aproximación a la mejor solución al problema.
    """
    
    poblacion = dominio.generar_n(tam_pobl)
    tam_elite = int(tam_pobl * porc_elite)

    for _ in range(reps):
        # Seleccionar las soluciones élite
        indices_elite = sorted(range(tam_pobl), key=lambda i: dominio.fcosto(poblacion[i]))[:tam_elite]
        elite = [poblacion[i] for i in indices_elite]

        # Generar nueva población mediante cruce y mutación
        nueva_poblacion = elite[:]

        while len(nueva_poblacion) < tam_pobl:
            if random.random() < prob_mut:
                # Mutar una solución
                sol = random.choice(elite)
                nueva_sol = dominio.mutar(sol)
            else:
                # Cruzar dos soluciones
                sol_a, sol_b = random.choices(elite, k=2)
                nueva_sol = dominio.cruzar(sol_a, sol_b)

            nueva_poblacion.append(nueva_sol)

        poblacion = nueva_poblacion

    # Seleccionar la mejor solución de la población final
    mejor_indice = min(range(tam_pobl), key=lambda i: dominio.fcosto(poblacion[i]))
    mejor_solucion = poblacion[mejor_indice]

    return mejor_solucion

