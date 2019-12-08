from sys import stderr

MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

def numero_mes(nombre_mes):

    return MESES.index(nombre_mes) + 1


def leer_fechas(nombre_archivo):
    fechas = []
    with open(nombre_archivo, 'r') as fichero:
        for linea in fichero:
            fecha = calcula_fecha(linea[:-1])
            fechas.append(fecha)

    return fechas

def calcula_fecha(cad):
    partes = cad.split()
    dia, mes, anyo = partes[0], partes[1], partes[2]

    return int(dia), numero_mes(mes), int(anyo)

DIA = 0
MES = 1
ANYO = 2
def menor_fecha(fechas):
    menor = None
    for fecha in fechas:
        dia, mes, anyo = fecha
        if menor == None or menor[ANYO] > anyo or \
            (menor[ANYO] == anyo and menor[MES] > mes) or \
            (menor[ANYO] == anyo and menor[MES] == mes and menor[DIA] > dia):
            menor = fecha
    return menor


def mayor_fecha(fechas):
    mayor = None
    for fecha in fechas:
        dia, mes, anyo = fecha
        if mayor == None or mayor[ANYO] < anyo or \
            (mayor[ANYO] == anyo and mayor[MES] < mes) or \
            (mayor[ANYO] == anyo and mayor[MES] == mes and mayor[DIA] < dia):
            mayor = fecha
    return mayor


def fecha_a_cadena(fecha):
    return '{0} {1} {2}'.format(fecha[DIA], MESES[fecha[MES] - 1], fecha[ANYO])


fechas = leer_fechas('fechas.txt')
menor = menor_fecha(fechas)
mayor = mayor_fecha(fechas)
print('La menor fecha es {0}'.format(fecha_a_cadena(menor)))
print('La mayor fecha es {0}'.format(fecha_a_cadena(mayor)))