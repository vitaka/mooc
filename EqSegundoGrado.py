from utils import eq_seg_grado
from sys import stderr


def pide_fact_eq():
    try:
        a = float(input('Introduce el factor a: '))
        b = float(input('Introduce el factor b: '))
        c = float(input('Introduce el factor c: '))

        return a, b, c
    except ValueError as e:
        raise ValueError('¡Debe introducir un número!')


try:
    a, b, c = pide_fact_eq()
    x1, x2 = eq_seg_grado(a, b, c)
    print('Uno de los resultados de la ecuación es ', x1, ' y el otro es ', x2)
except ValueError as e:
    print(e, file=stderr)
