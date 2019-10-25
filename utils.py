from math import sqrt
from random import randint


def calcula_pi():
    return 3.141596

pi = calcula_pi()


def eq_seg_grado(a, b, c):
    try:
        tmp = sqrt(b ** 2 - 4 * a * c)

        x1 = (-b + tmp) / (2 * a)
        x2 = (-b - tmp) / (2 * a)

        return x1, x2
    except ValueError as e:
        raise ValueError('Esa ecuación de segundo orden no tiene soluciones.')
    except ZeroDivisionError as e:
        raise ValueError('El valor de a no puede ser cero.')


def area_rect(width, height):
    area = width * height
    return area


def area_cuadrado(width):
    return area_rect(width, width)


def area_triang_rect(width, height):
    return area_rect(width, height) / 2


def area_circulo(radio):
    return pi * radio ** 2


def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def encontrar_primos(num):
    lista = []
    for i in range(2, num + 1):
        if es_primo(i):
            lista.append(i)
    return lista


def suma_lista(lista):
    suma = 0
    for e in lista:
        suma += e
    return suma


def max_lista(lista):
    if len(lista) == 0:
        return None, None

    max, pos_max = lista[0], 0
    for i in range(1, len(lista)):
        if lista[i] > max:
            max, pos_max = lista[i], i

    return max, pos_max


def introduce_lista_nums(msg, div=',', type='FLOAT'):
    lista = []
    cad = input(msg)
    if cad == '':
        return []
    numbers = cad.split(div)
    for num in numbers:
        if type == 'FLOAT':
            lista.append(float(num))
        elif type == 'INT':
            lista.append((int(num)))
        else:
            raise ValueError('El parámetro type solo acepta INT o FLOAT')
    return lista


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


def matriz_unitaria(n):
    return matriz_diagonal(n)


def matriz_diagonal(n, valor=1):
    M  = []
    for i in range(n):
        row = [0] * n
        row[i] = valor
        M.append(row)
    return M


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


def int_matriz_random(n, m, min, max):
    M = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(randint(min, max))
        M.append(row)

    return M