M = [
    [5, 4, 1, 2, 8, 8, 1],
    [6, 4, 1, 3, 7, 5, 2],
    [7, 2, 2, 4, 5, 1, 3],
    [6, 6, 2, 1, 6, 2, 4],
    [5, 1, 2, 2, 1, 2, 1],
    [4, 3, 1, 2, 2, 1, 1]
]


def sec_max(lista):
    max_sec = 0
    contador = 1
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            contador += 1
            if max_sec < contador:
                max_sec = contador
        else:
            contador = 1

    return max_sec


def obtener_lista(matriz, fila, col, incfila, inccol):
    lista = []

    if incfila == 0 and inccol == 0:
        raise ValueError('Los valores de incrento de fila y de columna no pueden ser 0 simultáneamente.')

    while fila < len(M) and col < len(M[fila]) and fila >= 0 and col >= 0:
        lista.append(matriz[fila][col])
        fila += incfila
        col += inccol

    return lista


max = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        lista = obtener_lista(M, i, j, 0, 1)
        num = sec_max(lista)
        if max < num:
            max = num
        lista = obtener_lista(M, i, j, 1, 1)
        num = sec_max(lista)
        if max < num:
            max = num
        lista = obtener_lista(M, i, j, 1, 0)
        num = sec_max(lista)
        if max < num:
            max = num
        lista = obtener_lista(M, i, j, 1, -1)
        num = sec_max(lista)
        if max < num:
            max = num

print(max)