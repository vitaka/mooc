from sys import argv
from sys import stderr


try:
    file_name = argv[1]
    sum = 0
    for arg in argv[2:]:
        sum += float(arg)

    with open(file_name, 'w') as file:
        print('Resultado:', file=file)
        file.write(str(sum))
        file.write('Fin.')

    print('Bien hecho!')
    """
    file = open(file_name, 'w')
    file.write(str(sum))
    file.close()
    """
except IndexError as e:
    print('Error con los argumentos, este programa necesita dos números reales.', file=stderr)
    print('USO:', file=stderr)
    print(argv[0], 'FILE' 'NUM...', file=stderr)
