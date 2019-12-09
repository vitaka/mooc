from random import random

def matriz_aleatoria(n, m, max):
    M = []
    for i in range(n):
        lista = []
        for j in range(m):
            lista.append(random() * max)
        M.append(lista)

    return M


def print_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end = '\t')
        print()


n = int(input('Dame el número de filas: '))
m = int(input('Dame el número de columnas: '))
max = int(input('Dame el valor máximo aleatorio: '))

M = matriz_aleatoria(n, m, max)
print_matriz(M)
