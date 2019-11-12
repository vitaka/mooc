import matplotlib.pyplot as plt
from math import sin, pi

def seno_list(points):
    y = []
    for i in range(points):
        y.append(sin(i * 2 * pi / points))
    return y


y = seno_list(500)
plt.plot(y) # Dibuja el gráfico

plt.show() # Muestra la ventana