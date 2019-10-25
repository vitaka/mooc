from utils import introduce_lista_nums, imprime_matriz


def introduce_matriz():
    M = []

    row = None
    i = 1
    while row != []:
        row = introduce_lista_nums('Introduce la fila {0}: '.format(i), type='INT')
        if row != []:
            M.append(row)
            i += 1

    return M

M = introduce_matriz()
imprime_matriz(M)