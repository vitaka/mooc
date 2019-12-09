import numpy


n = int(input('Dame el número de filas: '))
m = int(input('Dame el número de columnas: '))
max = int(input('Dame el valor máximo aleatorio: '))

M = numpy.random.random() * max
print(M)