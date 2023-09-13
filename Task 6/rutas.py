def encontrar_ruta(C):
    #creamos una copia de mismo tamanno y la llena de 0
    solucion = matriz_vacia(C)
    #posicion inicial del ciclista en X
    posicion_inicialX = 0
    #posicion inicial del ciclista en Y
    posicion_inicialY = 0

    #llamada a funcion auxiliar para buscar una solucion
    if encontrar_ruta_aux(C, posicion_inicialX, posicion_inicialY, solucion):
        return solucion
    
    #si no hay solucion retorna una lista vacia
    return []

def encontrar_ruta_aux(C, i, j, solucion):
    #largo de filas
    filas = len(C)
    #largo de columnas
    columnas = len(C[0])

    # una vez llegamos al final de la matriz
    if i == filas - 1 and j == columnas - 1:
        #se marca la casilla inferior derecha como salida 
        solucion[i][j] = 1
        return True

    # si se sale del rango de la matriz en i o j (en i seria que se sale del rango por la izquierda y en j se sale por arriba)
    fuera_rango = -1
    # y si no hemos llegado al final y tanto en C como en la solucion estamos en una zona no peligrosa
    if fuera_rango < i and fuera_rango < j and i < filas and j < columnas and C[i][j] == 0 and solucion[i][j] == 0:

            # entonces encontramos una interseccion viable
            solucion[i][j] = 1

            #----------------------------backtracking-----------------------------

            # probamos a verificar si moviendonos a la derecha una interseccion es posible
            if encontrar_ruta_aux(C, i + 1, j, solucion):
                return True
            # probamos a verificar si moviendonos abajo una interseccion es posible
            if encontrar_ruta_aux(C, i, j + 1, solucion):
                return True
            # probamos a verificar si moviendonos arriba una interseccion es posible
            if encontrar_ruta_aux(C, i, j - 1, solucion):
                return True
            # probamos a verificar si moviendonos a la izquierda una interseccion es posible
            if encontrar_ruta_aux(C, i - 1, j, solucion):
                return True
            
            # sino no pasaremos por ese camino
            solucion[i][j] = 0
            # si no hay solucion
            return False

    
# funcion para crear matriz vacia del tamanno de C
def matriz_vacia(C):
    solucion = []
    
    #recorrido en filas
    for i in range(len(C)):
        fila = []
        #recorrido en columnas
        for j in range(len(C[0])):
            fila += [0]
        solucion += [fila]
    #retornamos la copia de la matriz
    return solucion
