import matplotlib.pyplot as plt
from math import sin, pi

def seno_list(points):
    y = []
    for i in range(points):
        y.append(sin(i * 2 * pi / points))
    return y


POINTS = 500
y = seno_list(POINTS)
plt.plot(y) # Dibuja el gráfico
# Indico, en el eje x en qué coordenadas quiero las etiquetas:
#    Primer parámetro: las posiciones de los 500 puntos que quiero colocar las etiquetas
#    Segundo parámetro: Las etiquetas a colocar
plt.xticks([0, POINTS/4, POINTS/2, POINTS * 3 / 4, POINTS], ['0', 'pi/2', 'pi', '3/2 pi', '2 pi'])
# Aleterantiva al anterior si en vez de en base a pi, al valor aproximado de pi redondeado a dos cifras decimales
# plt.xticks([0, POINTS/4, POINTS/2, POINTS * 3 / 4, POINTS], [0, round(pi/2, 2), round(pi, 2), round((pi * 3)/2, 2), round(2 * pi, 2)])
plt.show()