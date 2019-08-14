from sys import stderr
from utils import area_rect, area_triang_rect, area_cuadrado, area_circulo


def imprimir_menu():
    print('1. Calcular área rectángulo')
    print('2. Calcular área triángulo rectángulo')
    print('3. Calcular área cuadrado')
    print('4. Calcular área circunferencia')
    print('5. Salir')


op = '0'
while op != '5':
    imprimir_menu()
    op = input('Escoja opción: ')
    if op == '1':
        ancho = float(input('Dame el ancho del rectángulo: '))
        alto = float(input('Dame el alto del rectángulo: '))
        area = area_rect(ancho, alto)
        print('El área del rectángulo es', area)
    elif op == '2':
        base = float(input('Dame el base del triángulo rectángulo: '))
        alto = float(input('Dame el alto del triángulo rectángulo: '))
        area = area_triang_rect(base, alto)
        print('El área del rectángulo es', area)
    elif op == '3':
        ancho = float(input('Dame el ancho del cuadrado: '))
        area = area_cuadrado(ancho)
        print('El área del cuadrado es', area)
    elif op == '4':
        radio = float(input('Dame el radio de la circunferencia: '))
        area = area_circulo(radio)
        print('El área del círculo es', area)
    elif op == '5':
        print('Adiós, ¡hasta la próxima!')
    else:
        print('La opción seleccionada no es correcta.', file=stderr)
