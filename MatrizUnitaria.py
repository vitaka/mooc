def matriz_unitaria(n):
    return matriz_diagonal(n)


def matriz_diagonal(n, valor=1):
    M  = []
    for i in range(n):
        row = [0] * n
        row[i] = valor
        M.append(row)
    return M


def imprime_matriz(M):
    max_size = calcula_tam_maximo_num(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(('{0:' + str(max_size) + 'd}').format(M[i][j]), end=' ')
        print()


def calcula_tam_maximo_num(M):
    max = 0
    for row in M:
        for elem in row:
            s = str(elem)
            if len(s) > max:
                max = len(s)
    return max


unitaria = matriz_diagonal(10, 10)
unitaria[1][0] = 1000
imprime_matriz(unitaria)