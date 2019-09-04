from utils import encontrar_primos, suma_lista, max_lista


num = int(input('Dame un número: '))
primos = encontrar_primos(num)
result = suma_lista(primos)
print('La suma de la lista', primos, 'es', result)
for i in range(len(primos)):
    print('El primo nº', i + 1, 'es', primos[i])
max, pos = max_lista(primos)
print('El número más alto de esa lista es', max, 'y está en la posición', pos)



def suma_lista_par(lista1, lista2):
    i, j = 0, 0
    while i < len(lista1) and j < len(lista2):
        if lista2[j] % 2 != 0:
            lista1[i] += lista2[j]
            i += 1
            j += 1
        else:
            j += 1


lista = [2, 3, 4, 5, 6, 7, 8, 10, 20, 15]
suma_lista_par(primos, lista)
print(primos)


