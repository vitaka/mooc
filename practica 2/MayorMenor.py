from sys import stderr


def mayor_de_3(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            mayor = n1
        else:
            mayor = n3
    elif n2 > n3:
        mayor = n2
    else:
        mayor = n3

    return mayor


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


try:
    n1 = float(input('Introduce un número: '))
    n2 = float(input('Introduce otro número: '))
    n3 = float(input('Introduce el último número: '))

    mayor = mayor_de_3(n1, n2, n3)
    menor = menor_de_3(n1, n2, n3)

    print('El valor mayor de esos 3 números es {0} y el menor {1}'.format(mayor, menor))
except ValueError as e:
    print('Uno de los valores introducidos no es un valor numérico.', file=stderr)