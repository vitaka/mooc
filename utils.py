def calcula_pi():
    return 3.141596

pi = calcula_pi()


def eq_seg_grado(a, b, c):
    tmp = sqrt(b ** 2 - 4 * a * c)

    x1 = (-b + tmp) / 2 * a
    x2 = (-b - tmp) / 2 * a

    return x1, x2


def area_rect(width, height):
    area = width * height
    return area


def area_cuadrado(width):
    return area_rect(width, width)


def area_triang_rect(width, height):
    return area_rect(width, height) / 2


def area_circulo(radio):
    return pi * radio ** 2

