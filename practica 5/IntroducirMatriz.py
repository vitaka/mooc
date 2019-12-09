from utils import str_to_num_list
from sys import stderr


def introduce_matriz():
    M = []
    i = 1
    cad = ' '
    while not cad == '':
        cad = input('Dame la fila {0}: '.format(i))
        try:
            if not cad == '':
              M.append(str_to_num_list(cad))
              i += 1
        except ValueError as e:
            print(e, file=stderr)

    return M


M = introduce_matriz()

print(M)