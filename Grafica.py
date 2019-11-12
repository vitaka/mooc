import matplotlib.pyplot as plt
from math import sin, pi

def seno_list(points):
    y = []
    x = []
    for i in range(points):
        y.append(sin(i * 2 * pi / points))
        x.append(i * 2 * pi / points)
    return x, y


lista1 = [11,2,3,15,8,13,21,34] # Declara lista1 con 8 valores
plt.plot(lista1) # Dibuja el gráfico
plt.xlabel("abscisa") # Inserta el título del eje X
plt.ylabel("ordenada") # Inserta el título del eje Y
lista2 = [2,3,4,2,3,6,4,10] # Declara lista2 con 8 valores
plt.plot(lista2) # Dibuja datos de lista2
plt.title("Gráfica") # Establece nuevo título pero no muestra en gráfico
plt.grid(True) # Activa cuadrícula del gráfico pero no se muestra
plt.plot(lista1, label="Suspendidos")
plt.plot(lista2, label="Aprobados")

plt.xticks(range(8), ("A", "B", "C", "D", "E", "F", "G", "H"))
plt.yticks(range(0,51,10))

plt.legend()

plt.show()