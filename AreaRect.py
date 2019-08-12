from utils import area_rect, area_triang_rect, area_circulo


ancho = float(input('Introduce el ancho del rectángulo: '))
alto = float(input('Introduce el alto del rectángulo: '))

width = 100

result = area_rect(ancho, alto)
result2 = area_rect(50, 3)
print('El área de un rectángulo de', ancho, 'por', alto, 'es', result)
print('El area del triángulo rectángulo equivalente es', area_triang_rect(ancho, alto))
print('El área de un círculo con el radio igual a ese ancho es', area_circulo(ancho))
