from utils import str_to_num_list
from sys import stderr
from math import sqrt


def modulo(lista):
    sum = 0
    for e in lista:
        sum += e ** 2

    return sqrt(sum)


cad = input('Dame un vector: ')
try:
    lista = str_to_num_list(cad)
    print('El módulo del vector es {0}.'.format(modulo(lista)))
except ValueError as e:
    print(e, file=stderr)