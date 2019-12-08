from sys import stderr


def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

try:
    num = int(input('Dame un número entero: '))

    if es_primo(num):
        print("El número {0} es primo.".format(num))
    else:
        print('El número {0} NO es primo'.format(num))
except ValueError as e:
    print('El valor introducido no es un número entero.', file=stderr)