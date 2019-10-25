from utils import imprime_matriz
from sys import stderr
from time import sleep


def rellena_matriz_int(n, m, valor):
    M = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(valor)
        M.append(row)
    return M


def ganador(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != VACIO:
                for ficha in [ROJA, AZUL]:
                    if cuenta_fichas(tablero, i, j, 1, -1, ficha) == 4:
                        return ficha
                    if cuenta_fichas(tablero, i, j, 1, 0, ficha) == 4:
                        return ficha
                    if cuenta_fichas(tablero, i, j, 1, 1, ficha) == 4:
                        return ficha
                    if cuenta_fichas(tablero, i, j, 0, 1, ficha) == 4:
                        return ficha
    return None


def cuenta_fichas(tablero, y, x, incy, incx, ficha):
    contar = 0
    while y >= 0 and y < len(tablero) and x >= 0 and x < len(tablero[0]) \
            and tablero[y][x] == ficha:
        contar += 1
        x += incx
        y += incy
    return contar


def tablero_lleno(tablero):
    return 0 not in tablero[0]
    """
    for e in tablero[0]:
        if e == VACIO:
            return False
    return True
    """

def coloca_ficha(tablero, col, ficha):
    if tablero[0][col] != VACIO:
        raise ValueError('Esa columna no tiene espacio.')
    for i in range(1, len(tablero)):
        if tablero[i][col] != VACIO:
            tablero[i - 1][col] = ficha
            return tablero
    tablero[5][col] = ficha
    return tablero


def imprime_cabecera():
    for i in range(1, 8):
        print(i, end=' ')
    print()


def imprime_tablero(tablero):
    imprime_cabecera()
    imprime_matriz(tablero)

def error(msg):
    print(msg, file=stderr)
    sleep(1)


VACIO = 0
ROJA = 1
AZUL = 2

ficha = ROJA
tablero = rellena_matriz_int(6, 7, 0)

while ganador(tablero) == None and not tablero_lleno(tablero):
    imprime_tablero(tablero)
    try:
        col = int(input('Dime la columna a colocar la ficha {0}: '.
                        format('ROJA' if ficha == ROJA else 'AZUL')))
        if 1 <= col <= 7:
            try:
                coloca_ficha(tablero, col - 1, ficha)
                ficha = ROJA if ficha == AZUL else AZUL
            except ValueError as e:
                error(e)
        else:
            error('La columna debe ser entre 1 y 7')
    except ValueError as e:
        error('Debe introducir un número, vuelva a intentarlo')


imprime_tablero(tablero)
if ganador(tablero) == ROJA:
    print('El ganador es la ficha ROJA')
else:
    print('El ganador es la ficha AZUL')
