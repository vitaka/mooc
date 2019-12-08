cad = input('Dame una frase: ')

for c in cad:
    if c == 'a':
        print('o', end='')
    else:
        print(c, end='')
print()