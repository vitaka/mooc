from sys import argv
from sys import stderr


try:
    num1 = float(argv[1])
    num2 = float(argv[2])

    print(num1 + num2)
except (IndexError, ValueError) as e:
    print('Error con los argumentos, este programa necesita dos números reales.', file=stderr)
    print('USO:', file=stderr)
    print(argv[0], 'num1', 'num2', file=stderr)
