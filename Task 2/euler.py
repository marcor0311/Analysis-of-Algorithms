import math
import sys 
sys.setrecursionlimit(100000)

def e_cuadratica(euler):
    sumatoria = 0
    for i in range(euler):
        termino = 1/math.factorial(i)
        sumatoria = sumatoria + termino

    return sumatoria

def e_lineal(iteracion):
    return 2 + 1/e_lineal_aux(1, iteracion)

def e_lineal_aux(cola, iteracion):
    if cola == iteracion:
        return cola + cola/(cola+1)
    else:
        return cola + cola/(e_lineal_aux(cola+1, iteracion))
