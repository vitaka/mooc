from random import randint
from utils import imprime_matriz


def int_matriz_random(n, m, min, max):
    M = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(randint(min, max))
        M.append(row)

    return M


M = int_matriz_random(5, 6, 0, 10)
imprime_matriz(M)