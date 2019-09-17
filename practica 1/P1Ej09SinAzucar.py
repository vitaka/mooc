def menu():
    print('1. Una galleta')
    print('2. Una lata de Red Bull')
    print('3. Una cucharada de miel')
    print('4. Una rebandada con nocilla')
    print('5. Una rebandada con mermelada')

    opcion = int(input('Escoge una opción entre 1 y 5: '))
    return opcion


def dame_cantidad(opcion):
    if opcion == 1:
        cantidad = int(input('¿Cuántas galletas vas a tomar? '))
    elif opcion == 2:
        cantidad = int(input('¿Cuántas latas de Red Bull vas a tomar? '))
    elif opcion == 3:
        cantidad = int(input('¿Cuántas cucharadas te vas a poner? '))
    elif opcion == 4:
        cantidad = int(input('¿Cuántas rebanadas con nocilla vas a comer? '))
    elif opcion == 5:
        cantidad = int(input('¿Cuántas rebanadas con mermeladas vas a comer? '))

    return cantidad


def calcular_azucar(opcion, cantidad):
    if opcion == 1:
        return 1.5 * cantidad
    if opcion == 2:
        return 52 * cantidad
    if opcion == 3:
        return 24 * cantidad
    if opcion == 4:
        return 24 * cantidad
    if opcion == 5:
        return 9 * cantidad


op = menu()
cant = dame_cantidad(op)
azucar = calcular_azucar(op, cant)
if azucar > 25:
    print('Con estas cantidades consumes más de los 25g de azúcar al día que recomienda la OMS.')
else:
    print('¡Enhorabuena! Consumes menos de la cantidad máxima recomendada por la OMS.')
