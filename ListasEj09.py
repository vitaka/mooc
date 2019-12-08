lista = [0, 1, 1, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0 ,0]

def sec_max(lista):
    max_sec = 0
    contador = 1
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            contador += 1
            if max_sec < contador:
                max_sec = contador
        else:
            contador = 1

    return max_sec


num = sec_max(lista)

print('La secuencia más larga de la lista tiene un tamaño de {0}'.format(num))