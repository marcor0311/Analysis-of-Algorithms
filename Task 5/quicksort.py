import random

def separar(A, menor, mayor):

    pivote = A[mayor]

    i = menor - 1

    for j in range(menor, mayor):

        if A[j] <= pivote:

            i = i + 1

            (A[i], A[j]) = (A[j], A[i])

    (A[i + 1], A[mayor]) = (A[mayor], A[i + 1])

    return i + 1

 
def quicksort_aux(A, menor, mayor):

    if menor < mayor:

        pivote = separar(A, menor, mayor)

        quicksort_aux(A, menor, pivote - 1)

        quicksort_aux(A, pivote + 1, mayor)



def quicksort(A):
    menor = 0
    mayor = len(A)-1
    quicksort_aux(A, menor, mayor)
    return A

#######################################################################
def separacion_mejorada(A, inicio, final):
    i = inicio-1 
    pivote = A[ (inicio+final)//2]
    j = final+1 
    while True:
        i+=1
        while (A[i] < pivote):
            i+=1
        j-=1
        while (A[j]> pivote):
            j-=1
        if i>=j:
            return j
        A[i], A[j] = A[j], A[i] 
def quicksort_mejoradoAux(A, inicio, final):
    if inicio < final:
        p = separacion_mejorada(A, inicio, final)
        quicksort_mejoradoAux(A, inicio, p)
        quicksort_mejoradoAux(A, p+1, final)

def quicksort_mejorado(A):
    quicksort_mejoradoAux(A, 0, len(A)-1)
    return A
