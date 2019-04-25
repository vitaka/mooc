d = float(input('Dime la distancia recorrida: '))
t = float(input('Dime lo que ha tardado: '))
v = d/t

nueva_d = float(input('Introduce la distancia que recorrera el coche: '))

t_calculado = nueva_d / v

print('El coche tardará en recorrer', nueva_d, 'km en', t_calculado, 'hrs a la velocidad de', v, 'km/h.')