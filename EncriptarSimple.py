def encriptar(texto):
    enc = ''
    for c in texto:
        num = ord(c)
        num += 1
        enc += chr(num)

    return enc


cad = input('Dame un texto: ')

print(encriptar(cad))
