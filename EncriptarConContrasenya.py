def encriptar_texto(texto, password):
    i = 0
    for c in texto:
        ord_car = ord(c)
        ord_pass = ord(password[i % len(password)])
        new_car = chr(ord_car + ord_pass)
        print(new_car, end='')
        i += 1
    print()



texto = input('Introduce el texto a encriptar: ')
password = input('Introduce la contraseña: ')

encriptar_texto(texto, password)
