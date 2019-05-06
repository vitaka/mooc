from sys import stderr


def cambio(cantidad, tipo):
    billetes = cantidad // tipo
    resto = cantidad % tipo

    return billetes, resto


def imprime_cantidad_cambio(cantidad, nombre_tipo, tipo):
    if cantidad > 0:
        print('{0} {1} de {2}.'.format(cantidad, nombre_tipo, tipo))



try:
    cantidad = int(input('Dame la cantidad de dinero: '))

    mon500, resto = cambio(cantidad, 500)
    mon200, resto = cambio(resto, 200)
    mon100, resto = cambio(resto, 100)
    mon50, resto = cambio(resto, 50)
    mon20, resto = cambio(resto, 20)
    mon10, resto = cambio(resto, 10)
    mon2, resto = cambio(resto, 2)
    mon1, resto = cambio(resto, 1)

    imprime_cantidad_cambio(mon500, "billetes", 500)
    imprime_cantidad_cambio(mon200, "billetes", 200)
    imprime_cantidad_cambio(mon100, "billetes", 100)
    imprime_cantidad_cambio(mon50, "billetes", 50)
    imprime_cantidad_cambio(mon20, "billetes", 20)
    imprime_cantidad_cambio(mon10, "billetes", 10)
    imprime_cantidad_cambio(mon2, "monedas", 2)
    imprime_cantidad_cambio(mon1, "monedas", 1)

except ValueError as e:
    print('El valor introducido no es un entero.', file=stderr)







