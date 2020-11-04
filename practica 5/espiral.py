def espiral(M):
    result=[]

    n_filas=len(M)
    n_columnas=len(M[0])

    n_it=n_filas//2

    for it in range(n_it):
        # ->
        #  columna:
        # it 0: 0 -> n_columnas -1
        # it 1: 1 -> n_columnas -2
        # ...
        # it i: i -> n_columnas-i-1
        for col in range(it,n_columnas-it):
            result.append(M[it][col])

        #  columna abajo
        # fila:
        # it 0: 1 -> n_filas -1
        # it 1: 2 -> n_filas-2
        # ...
        # it i: i+1 -> n_filas -i -1
        for fila in range(it+1,n_filas-it):
            result.append(M[fila][n_columnas-it-1])

        # <-

        # columna arriba

    return result

M=[
    [5,2,1,9,7,10,3],
    [3,7,1,2,2,8,6],
    [3,8,4,8,6,2,7],
    [4,6,7,6,7,8,2],
    [4,9,10,3,8,5,9],
    [2,10,3,10,4,6,6]
]
print(espiral(M))