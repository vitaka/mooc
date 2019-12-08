from sys import stderr


def area_circulo(radio):
    return pi * radio ** 2


def pide_imprime_area_circunferencia():
    r = float(input('Dame el radio de la circunferencia: '))

    print('El area de una circunferencia de radio {0} es {1}.'.format(r, area_circulo(r)))


def eq_segundo_grado(a, b, c):
    r = sqrt(b * b - 4 * a * c)
    x1 = (-b + r) / (2 * a)
    x2 = (-b - r) / (2 * a)
    return x1, -x2


def pide_imprime_ecuacion_segundo_grado():
    a = float(input("Dame el valor de a: "))
    b = float(input("Dame el valor de b: "))
    c = float(input("Dame el valor de c: "))

    x1, x2 = eq_segundo_grado(a, b, c)
    print("Los resultados son {0} y {1}".format(x1, x2))


def divisores_numero(num):
    l = []
    for i in range(1, num):
        if num % i == 0:
            l.append(i)
    return l


def calcula_pi(iteraciones):
    num = 0
    for i in range(iteraciones):
        if i % 2 == 0:
            num = num + (4 / (i * 2 + 1))
        else:
            num = num - (4 / (i * 2 + 1))
    return num


def imprime_pi():
    iteraciones = int(input('Dame el número de iteraciones para calcular pi: '))
    pi = calcula_pi(iteraciones)
    print(pi)


def pide_imprime_los_divisores_numero():
    num = int(input('Dame un número entero: '))
    l = divisores_numero(num)
    print('Los divisores de {0} son {1}.'.format(num, l))

def menu():
    print('1. El área de una circunferencia')
    print('2. Una ecuación de segundo grado')
    print('3. Los divisores de un número')
    print('4. Calcula el número PI mediante Gregory-Leibniz.')

    op = int(input('Escoge una opción: '))

    return op


try:
    op = menu()

    if op == 1:
        pide_imprime_area_circunferencia()
    elif op == 2:
        pide_imprime_ecuacion_segundo_grado()
    elif op == 3:
        pide_imprime_los_divisores_numero()
    elif op == 4:
        imprime_pi()
    else:
        print('Esa opción no es correcta.', file=stderr)
except ValueError as e:
    print('El valor introducido no es un número esperado.', file=stderr)