def imprimir_tabla(tabla):
    for i in range(1, 11):
        print(i, 'x', tabla, '=', i * tabla)
    print('\n')


for tabla in range(1, 11):
    imprimir_tabla(tabla)
