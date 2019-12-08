from sys import stderr


def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def calcula_lista_primos(num):
    l=[]

    for i in range(2, num + 1):
        if es_primo(i):
            l.append(i)
    return l


try:
    num = int(input('Introduce un número entero: '))

    lista_primos = calcula_lista_primos(num)

    print('Los primos igual o menores a {0} son {1}'.format(num, lista_primos))
except ValueError as e:
    print('El valor introducido no es un número entero.', file=stderr)