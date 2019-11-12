from time import sleep
from sys import stderr


def menu():
    print(ANYADIR, 'Añadir contacto')
    print(BORRAR, 'Borrar contacto')
    print(MODIFICAR, 'Modificar contacto')
    print(BUSCAR, 'Buscar contacto')
    print(LISTAR, 'Listar contacto')
    print(SALIR, 'Salir')
    try:
        op = int(input('Escoge una opción: '))
        return op
    except ValueError as e:
        return None


def introduce_contacto():
    nombre = input('Introduce un nombre: ')
    tel = input('Introduce un teléfono: ')
    dir = input('Introduce una dirección: ')
    email = input('Introduce un email: ')

    return nombre, tel, dir, email


def anyadir_contacto(agenda):
    contacto = introduce_contacto()
    nombre, tel, dir, email = contacto
    agenda[nombre] = contacto
    agenda[tel] = contacto
    agenda[email] = contacto
    contactos.append(contacto)


def buscar(agenda, nombre_a_buscar):
    for i in range(len(agenda)):
        contacto = agenda[i]
        nombre, tel, dir, email = contacto
        if nombre_a_buscar == nombre:
            return i

    return -1


def borrar_contacto(agenda):
    nombre = input('Introduce el nombre: ')
    try:
        del agenda[nombre]
    except KeyError as e:
        msg('Ese contacto no existe.')


def modificar_contacto(agenda):
    nombre = input('Introduce el nombre: ')
    if nombre in agenda:
        print('Introduce los nuevos datos de ese contacto.')
        contacto = introduce_contacto()
        agenda[nombre] = contacto
    else:
        msg('Ese contacto no existe.')


def msg(texto):
    print(texto, file=stderr)
    sleep(1)


def buscar_contacto(agenda):
    nombre = input('Buscar: ')

    try:
        contacto = agenda[nombre]
        imprime_contacto(contacto)
    except KeyError as e:
        msg('Ese contacto no existe.')


def imprime_contacto(contacto):
    nombre, tel, dir, email = contacto
    print('Nombre:', nombre)
    print('Teléfono:', tel)
    print('Dirección:', dir)
    print('email:', email)


def listar_contactos(contactos):
    for contacto in contactos:
        imprime_contacto(contacto)
        print()


ANYADIR = 1
BORRAR = 2
MODIFICAR = 3
BUSCAR = 4
LISTAR = 5
SALIR = 6
agenda = {}
contactos = []
op = None
while op != SALIR:
    op = menu()
    if op == ANYADIR:
        anyadir_contacto(agenda)
    elif op == BORRAR:
        borrar_contacto(agenda)
    elif op == MODIFICAR:
        modificar_contacto(agenda)
    elif op == BUSCAR:
        buscar_contacto(agenda)
    elif op == LISTAR:
        listar_contactos(contactos)
    elif op != SALIR:
        msg('Opción incorrecta, vuelva a intentarlo.')

print('Bye!')
