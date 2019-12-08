from sys import stderr

def introduce_int_list():
    lista = []
    cad = ''
    while cad != 'fin':
        cad = input('Introduce un número: ')
        if cad != 'fin':
            try:
                lista.append(int(cad))
            except ValueError as e:
                print('El dato introducido no es un número entero, '
                      'por favor vuelve a introducirlo o escribe "fin" para terminar.', file=stderr)

    return lista

lista = introduce_int_list()

print(lista)