def maximizar(As, D):
    As.sort(key=lambda x : x[1])
    cant_archivos = len(As)
    cardinalidad_max=[]
    suma=0
    for i in range(cant_archivos):
        suma += As[i][1]
        if suma <= D:
            archivo_almacenado = [As[i]]
            cardinalidad_max += (archivo_almacenado)
        elif suma > D:
            break
    return cardinalidad_max
