from math import sqrt


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

