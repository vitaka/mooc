from math import sqrt
from sys import stderr


def menor_de_3(n1, n2, n3):
    if n1 < n2:
        if n1 < n3:
            return n1
        else:
            return n3
    elif n2 < n3:
        return n2
    else:
        return n3


def distancia(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


try:
    x1=float(input('Dame la coordenada x del punto 1: '))
    y1=float(input('Dame la coordenada y del punto 1: '))
    x2=float(input('Dame la coordenada x del punto 2: '))
    y2=float(input('Dame la coordenada y del punto 2: '))
    x3=float(input('Dame la coordenada x del punto 3: '))
    y3=float(input('Dame la coordenada y del punto 3: '))

    d12 = distancia(x1, y1, x2, y2)
    d13 = distancia(x1, y1, x3, y3)
    d23 = distancia(x2, y2, x3, y3)

    d_min = menor_de_3(d12, d13, d23)

    if d_min == d12:
        print('Los puntos 1 y 2 son los más cercanos')
    elif d_min == d13:
        print('Los puntos 1 y 3 son los más cercanos')
    elif d_min == d23:
        print('Los puntos 2 y 3 son los más cercanos')
    else:
        print('Los tres puntos están a la misma distancia')
except ValueError as e:
    print('El valor introducido no es un número.', file=stderr)