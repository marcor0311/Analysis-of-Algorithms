import big_o
from big_o import complexities as cmpl
import math
import numpy as np
from random import shuffle
import unittest
import warnings
import sys
import importlib


from quicksort import quicksort, quicksort_mejorado

sys.setrecursionlimit(10000)

def generar_peor_caso(n):
    A = list(range(0, n))
    shuffle(A)
    return A

def generar_caso_promedio(n):
    A = list(range(0, n))
    shuffle(A)
    return A
          
def _graficar(fitted, titulo):
    xs = fitted['measures']
    ys = fitted['times']

    if importlib.util.find_spec('gnuplotlib') is not None:
        import gnuplotlib as gp
        gp.plot(xs, ys, _with='lines', terminal='dumb 60,30',
                unset='grid', title=titulo, xlabel='n', ylabel='tiempo')

    for k, v in fitted.items():
        if isinstance(k, big_o.complexities.ComplexityClass):
            residual = v
            r2 = 1 - residual / (ys.size * ys.var())
            print(k, f' (r={residual}, r^2={r2})')


class PruebasQuicksort(unittest.TestCase):

    def test_quicksort(self):
        A = [5, 3, 9, 0, 6, 2, 8, 1, 4, 7]
        O = quicksort(A)

        self.assertListEqual(O, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quicksort_mejorado(self):
        A = [5, 3, 9, 0, 6, 2, 8, 1, 4, 7]
        O = quicksort_mejorado(A)

        self.assertListEqual(O, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quicksort_dups(self):
        A = [5, 5, 3, 3, 9, 9, 0, 0, 6, 6, 2, 2, 8, 8, 1, 1, 4, 4, 7, 7]
        O = quicksort(A)

        self.assertListEqual(O, [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])

    def test_quicksort_mejorado_dups(self):
        A = [5, 5, 3, 3, 9, 9, 0, 0, 6, 6, 2, 2, 8, 8, 1, 1, 4, 4, 7, 7]
        O = quicksort_mejorado(A)

        self.assertListEqual(O, [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])

    def test_quicksort_trivial(self):
        A = [5]
        O = quicksort(A)

        self.assertListEqual(O, [5])


    def test_quicksort_mejorado_trivial(self):
        A = [5]
        O = quicksort_mejorado(A)

        self.assertListEqual(O, [5])

    def test_quicksort_vacio(self):
        A = []
        O = quicksort(A)

        self.assertListEqual(O, [])


    def test_quicksort_mejorado_vacio(self):
        A = []
        O = quicksort_mejorado(A)

        self.assertListEqual(O, [])

    def test_peor_caso(self):
        best, fitted = big_o.big_o(quicksort, generar_peor_caso, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linearithmic, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, "Peor caso")

        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadrática, complejidad estimada {best}')


    def test_caso_promedio(self):
        best, fitted = big_o.big_o(quicksort_mejorado, generar_caso_promedio, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Quadratic, cmpl.Linearithmic], return_raw_data=True)

        _graficar(fitted, "Caso promedio")

        if not isinstance(best, big_o.complexities.Linearithmic):
            warnings.warn(
                f'Complejidad esperada Linearítmica, complejidad estimada {best}')

    def test_peor_caso_mejorado(self):
        best, fitted = big_o.big_o(quicksort_mejorado, generar_peor_caso, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linearithmic, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, "Peor caso con quicksort mejorado")

        if not isinstance(best, big_o.complexities.Linearithmic):
            warnings.warn(
                f'Complejidad esperada Linearítmica, complejidad estimada {best}')
