def encripta_cadena(cad, num):
    for c in cad:
        ord_car = ord(c)
        car_encr = chr(ord_car + num)
        print(car_encr, end='')
    print()

try:
    cad = input('Dame la frase a encriptar: ')
    num = int(input('Cuántos caracteres quieres adelantar: '))

    encripta_cadena(cad, num)
except ValueError as e:
    print('El número de caracteres a adelantar debe ser un valor entero.')