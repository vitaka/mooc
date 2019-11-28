from time import sleep
from sys import stderr, argv


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
    if nombre not in agenda:
        agenda[nombre] = [contacto]
    else:
        agenda[nombre].append(contacto)


def borrar_contacto(agenda):
    nombre = input('Introduce el nombre: ')
    try:
        listar_contactos(agenda[nombre], enum=True)
        pos = int(input('Número de contacto a borrar: '))
        if 0 < pos <= len(agenda[nombre]):
            del agenda[nombre][pos - 1]
        else:
            msg('Ese número de contacto no existe')
    except KeyError as e:
        msg('Ese contacto no existe.')
    except ValueError as e:
        msg('Debes introducir un número.')



def modificar_contacto(agenda):
    try:
        nombre = input('Introduce el nombre: ')
        if nombre in agenda:
            listar_contactos(agenda[nombre], enum=True)
            pos = int(input('Número de contacto a modificar: '))
            if 0 < pos <= len(agenda[nombre]):
                print('Introduce los nuevos datos de ese contacto.')
                contacto = introduce_contacto()
                agenda[nombre][pos - 1] = contacto
            else:
                msg('Ese número de contacto no existe')
        else:
            msg('Ese contacto no existe.')
    except ValueError as e:
        msg('Debes introducir un número.')


def msg(texto):
    print(texto, file=stderr)
    sleep(1)


def buscar_contacto(agenda):
    nombre = input('Buscar: ')

    try:
        contactos = agenda[nombre]
        listar_contactos(contactos)
    except KeyError as e:
        msg('Ese contacto no existe.')


def imprime_contacto(contacto):
    nombre, tel, dir, email = contacto
    print('Nombre:', nombre)
    print('Teléfono:', tel)
    print('Dirección:', dir)
    print('email:', email)


def listar_contactos(contactos, enum=False):
    for i in range(len(contactos)):
        if enum:
            print('CONTACTO', i + 1)
        imprime_contacto(contactos[i])
        print()

def listar_agenda(agenda):
    for nombre in agenda:
        listar_contactos(agenda[nombre])


def parseArgs(argv):
    if len(argv) >= 2:
        return argv[1]
    raise ValueError('Esta aplicación necesita un argumento con el archivo de agenda.')


def saveAgenda(agenda, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for nombre in agenda:
            print(nombre, end=':', file=file)
            # file.write(nombre + ':')
            save_contacts(agenda[nombre], file)


def save_contacts(contactos, file):
    for contacto in contactos:
        nombre, telefono, dir, email = contacto
        if contacto == contactos[-1]:
            print(nombre, telefono, dir, email, sep=',', file=file)
        else:
            print(nombre, telefono, dir, email, sep=',', end=';', file=file)

def loadAgenda(file_name):
    agenda = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line) > 0:
                nombre, contactos = descompone_contacto_agenda(line)
                agenda[nombre] = contactos

    return agenda


def descompone_contacto_agenda(line):
    contacto_agenda = line.split(':')
    nombre = contacto_agenda[0]
    contactos = descompone_contactos(contacto_agenda[1])
    return nombre, contactos


def descompone_contactos(contactos_line):
    result = []
    contactos = contactos_line.replace('\n','').split(';')
    for contacto in contactos:
        elems = contacto.split(',')
        result.append( (elems[0], elems[1], elems[2], elems[3]) )

    return result


ANYADIR = 1
BORRAR = 2
MODIFICAR = 3
BUSCAR = 4
LISTAR = 5
SALIR = 6

try:
    file = parseArgs(argv)
    agenda = loadAgenda(file)

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
            listar_agenda(agenda)
        elif op != SALIR:
            msg('Opción incorrecta, vuelva a intentarlo.')
    saveAgenda(agenda, file)
except ValueError as e:
    print(e, file=stderr)

print('Bye!')
