def contar_rutas_mas_cortas(C):
    if C[0][0] == 1:
        return 0
    else:
        filas,columnas = len(C),len(C[0])

    for i in range(filas):
        if C[i][0] == 1:
            C[i][0] = 0
        elif C[i][0] == 0:
            C[i][0] = 1
    for j in range(1, columnas):
        if C[0][j] == 1:
            C[0][j] = 0
        elif C[0][j] == 0:
            C[0][j] = 1

    for i in range(1, filas):
        for j in range(1, columnas):
            if C[i][j] == 1:
                C[i][j] = 0
            elif C[i][j] == 0:
                C[i][j] = C[i - 1][j] + C[i][j - 1]
    return C[filas - 1][columnas - 1]
