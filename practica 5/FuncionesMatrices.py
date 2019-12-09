from random import random


def suma_matrices(m1, m2):
    if len(m1) != len(m2):
        raise ValueError('Las matrices no tienen el mismo número de filas.')
    matriz=[]
    for y in range(len(m1)):
        fila=[]
        if len(m1[y]) != len(m2[y]):
            raise ValueError('Las matrices no tienen el mismo número de columnas.')
        for x in range(len(m1[y])):
            fila.append(m1[y][x] + m2[y][x])
        matriz.append(fila)
    return matriz


def resta_matrices(m1, m2):
    if len(m1) != len(m2):
        raise ValueError('Las matrices no tienen el mismo número de filas.')
    matriz=[]
    for y in range(len(m1)):
        fila=[]
        if len(m1[y]) != len(m2[y]):
            raise ValueError('Las matrices no tienen el mismo número de columnas.')
        for x in range(len(m1[y])):
            fila.append(m1[y][x] - m2[y][x])
        matriz.append(fila)
    return matriz


def multiplicacion_matrices(m1, m2):
    matriz=[]
    for i in range(len(m1)):
        matriz.append([])
        if len(m2) == 0 or len(m1[i]) != len(m2):
            raise ValueError('El número de filas de la primera matriz debe ser igual al número de columnas de la segunda.')
        for j in range(len(m1[i])):
            matriz[i].append(0)
            for k in range(len(m2)):
                if k >= len(m1[i]) or i >= len(m2[k]):
                    raise ValueError('El número de filas de la primera matriz debe ser igual al número de columnas de la segunda.')
                matriz[i][j] += m1[i][k] * m2[k][i]
    return matriz


def rellena_matriz(min, max, n ,m):
    matriz=[]
    for y in range(m):
        fila=[]
        for x in range(n):
            fila.append(random()*(max-min)+min)
        matriz.append(fila)
    return matriz


M = rellena_matriz(0, 100, 10, 5)
N = rellena_matriz(0, 100, 5, 10)
P = multiplicacion_matrices(M, N)
print(P)