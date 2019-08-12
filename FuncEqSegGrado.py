from math import sqrt


def eq_seg_grado(a, b, c):
    tmp = sqrt(b ** 2 - 4 * a * c)

    x1 = (-b + tmp) / 2 * a
    x2 = (-b - tmp) / 2 * a

    return x1, x2


a = float(input('Introduce el factor a: '))
b = float(input('Introduce el factor b: '))
c = float(input('Introduce el factor c: '))

result1, result2 = eq_seg_grado(a, b, c)
print('Las raices de esa ecuación son ', result1, 'y', result2)
result1, result2 = eq_seg_grado(3, 10, 2)
