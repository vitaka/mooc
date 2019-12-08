from sys import stderr


def pide_password():
    for i in range(1, 4):
        email = input('Introduce tu email: ')
        if email == 'fin':
            return False

        password = input('Introduce la contraseña: ')

        if email == 'a@b.c' and password == 'micontraseña':
            return True
        print('El correo y contraseña introducidos no son válidos', file=stderr)
    return False


if pide_password():
    print('Acceso satisfactorio')
else:
    print('Acceso denegado', file=stderr)