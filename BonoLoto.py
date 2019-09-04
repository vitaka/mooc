from sys import stderr
from random import randint


def pide_numeros(max):
    lista = []
    while len(lista) < max:
        try:
            num = int(input('Introduce un número entre 1 y 49: '))
            if num >= 1 and num <= 49:
                if num not in lista:
                    lista.append(num)
                else:
                    print('Ese número ya ha sido introducido, vuelve a introducir uno diferente', file=stderr)
            else:
                print('El número debe ser entre 1 y 49, vuelva a intentarlo', file=stderr)
        except ValueError as e:
            print('El dato introducido no es un número, vuelve a intentarlo.', file=stderr)
    return lista


def genera_nums(max):
    lista = []
    while len(lista) < max:
        num = randint(1, 49)
        if num not in lista:
            lista.append(num)
    return lista


def coincidencias(lista1, lista2):
    count = 0
    for num in lista1:
        if num in lista2:
            count += 1
    return count


MAX_NUMS = 6
usu_nums = pide_numeros(MAX_NUMS)
rand_nums = genera_nums(MAX_NUMS)
aciertos = coincidencias(usu_nums, rand_nums)
print('Has coincido en', aciertos, 'numeros')
print('Los números introducidos por el usuario son:', usu_nums)
print('Los números obtenidos en el sorteo son', rand_nums)
