from sys import stderr
from pintarTablero import  setup_tablero,pinta_ficha


### Constantes ###
VACIO = 0
ROJA = 1
AMARILLA = 2

NFILAS=6
NCOLS=7

### Función auxiliar para imprimir matriz ####
def calcula_tam_maximo_num(M):
    max = 0
    for row in M:
        for elem in row:
            s = str(elem)
            if len(s) > max:
                max = len(s)
    return max

### Imprime una matriz por salida estándar ###
def imprime_matriz(M):
    max_size = calcula_tam_maximo_num(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(('{0:' + str(max_size) + 'd}').format(M[i][j]), end=' ')
        print()

### Crea una matriz de n filas y m columnas que contiene "valor" en todas sus posiciones ###
def rellena_matriz_int(n, m, valor):
    M = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(valor)
        M.append(row)
    return M

### Comprueba si algún jugador ha ganado ##
# Devuelve el número que representa el color de la ficha del ganador, si lo hay.
# Si no hay ganador, devuelve None
def ganador(tablero):
    for ficha in [ROJA, AMARILLA]:
        if max_fichas(tablero,ficha) >= 4:
            return ficha
    return None

### Cuenta el número de fichas consecutivas de un color dado ###
# y,x: casilla de partida
# incy, incx: dirección en la que buscar las fichas
# ficha: color de la ficha
def cuenta_fichas(tablero, y, x, incy, incx, ficha):
    contar = 0
    while y >= 0 and y < len(tablero) and x >= 0 and x < len(tablero[0]) \
            and tablero[y][x] == ficha:
        contar += 1
        x += incx
        y += incy
    return contar

### Cuenta el número de fichas consecutivas de un color dado en cualquier dirección y lugar del tablero ###
def max_fichas(tablero,ficha):
    maxf=0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != VACIO:
                cuentas=[]
                cuentas.append(cuenta_fichas(tablero, i, j, 1, 1, ficha))
                cuentas.append(cuenta_fichas(tablero, i, j, 1, -1, ficha))
                cuentas.append(cuenta_fichas(tablero, i, j, 1, 0, ficha))
                cuentas.append(cuenta_fichas(tablero, i, j, 0, 1, ficha))
                if max(cuentas) > maxf:
                    maxf = max(cuentas)
    return maxf

### Devuelve True si ya no se pueden insertar más fichas en el tablero y False en caso contrario ###
def tablero_lleno(tablero):
    return 0 not in tablero[0]

### Modifica el tablero con la inserción de la ficha "ficha" en la columna "col" ###
def coloca_ficha(tablero, col, ficha, pintar=False):
    # Para el acceso al tablero, los índices empiezan en 0
    col=col-1
    if tablero[0][col] != VACIO:
        raise ValueError('Esa columna no tiene espacio.')
    for i in range(1, len(tablero)):
        if tablero[i][col] != VACIO:
            tablero[i - 1][col] = ficha
            if pintar:
                pinta_ficha(col+1,i, 'red' if ficha == ROJA else 'yellow')
            return tablero
    tablero[5][col] = ficha
    #pinta ficha recibe valores que empiezan en 1
    if pintar:
        pinta_ficha(col+1, 6,'red' if ficha == ROJA else 'yellow')
    return tablero

### Copia un tablero, de manera que modificaciones en la variable que devuelve no afectan al tablero original  ###
def copiar_tablero(tablero):
    t=[]
    for fila in tablero:
        f=[]
        for e in fila:
            f.append(e)
        t.append(f)
    return t

### Imprime cabecera del tablero por salida estándar ###
def imprime_cabecera():
    for i in range(1, 8):
        print(i, end=' ')
    print()

### Imprime tablero entero por salida estándar ###
def imprime_tablero(tablero):
    imprime_cabecera()
    imprime_matriz(tablero)

def error(msg):
    print(msg, file=stderr)

############ Calcula mejor jugada según se planteó en el segundo parcial ##############
def mejores_posiciones_examen(tablero,mificha):
    mejores_jugadas = []
    max_consecutivas_posibles = 0
    for i in range(1, NCOLS + 1):
        nuevoTablero = copiar_tablero(tablero)
        coloca_ficha(nuevoTablero, i , mificha)
        num_cons= max_fichas(nuevoTablero,mificha)
        if num_cons > max_consecutivas_posibles:
            mejores_jugadas=[i]
            max_consecutivas_posibles=num_cons
        elif num_cons == max_consecutivas_posibles:
            mejores_jugadas.append(i)
    return max_consecutivas_posibles,mejores_jugadas



############# Funciones para calcular mejor jugada con recursividad ##############

def puntuacion_tablero(tablero,mificha,fichaoponente):
    # Primer aproximación la puntuación será el máximo número de mis fichas consecutivas menos las de mi oponente
    # 100 si he ganado
    # -100 si he perdido
    g=ganador(tablero)
    if g == mificha:
        return 100
    elif g == fichaoponente:
        return -100
    else:
        return max_fichas(tablero,mificha) - max_fichas(tablero,fichaoponente)


####### Algoritmo recursivo que no tiene en cuenta que el oponente va a intentar jugar de la mejor manera posible ######
def mejor_puntuacion(tablero, mificha,fichaoponente, quienjuega, maxturnos):
    if maxturnos == 0 or ganador(tablero) is not None or tablero_lleno(tablero):
        return puntuacion_tablero(tablero,mificha,fichaoponente),[]

    if mificha == quienjuega:
        sig_jugador=fichaoponente
    else:
        sig_jugador=mificha

    puntuaciones=[]
    for i in range(1,NCOLS+1):
        #El tablero empieza por 0, solo considero jugadas en las columnas donde hay hueco
        if tablero[0][i-1] == VACIO:
            nuevoTablero=copiar_tablero(tablero)
            coloca_ficha(nuevoTablero,i,quienjuega)
            punt, movs = mejor_puntuacion(nuevoTablero, mificha, fichaoponente, sig_jugador, maxturnos - 1)
            puntuaciones.append((punt,[i]+movs ))

    #Máxima puntuación
    max_punt=None
    col_max_punt=None
    for tup_punt in puntuaciones:
        if max_punt is None:
            max_punt=tup_punt[0]
            col_max_punt=tup_punt[1]
        elif tup_punt[0] > max_punt:
            max_punt = tup_punt[0]
            col_max_punt = tup_punt[1]
    return max_punt,col_max_punt


####### Algoritmo recursivo que tiene en cuenta que el oponente va a intentar jugar de la mejor manera posible ######
# tablero: matriz con el tablero
# mificha: identificador de mi ficha en el tablero
# fichaoponente: identificador de la ficha del oponente en el tablero
# quienjuega: identificador de la ficha que se va a introducir en la siguiente jugada
# maxturnos: máximo de llamadas recursivas que podemos realizar
def mejor_puntuacion_2(tablero, mificha,fichaoponente, quienjuega, maxturnos):
    #Casos base:
    # - Ya he agotado el máximo de turnos que puedo calcular
    # - Ya hay ganador
    # - El tablero está lleno
    if maxturnos == 0 or ganador(tablero) is not None or tablero_lleno(tablero):
        return puntuacion_tablero(tablero,mificha,fichaoponente),[]

    # Calculo
    if mificha == quienjuega:
        sig_jugador=fichaoponente
    else:
        sig_jugador=mificha

    puntuaciones=[]
    for i in range(1,NCOLS+1):
        #El tablero empieza por 0, solo considero jugadas en las columnas donde hay hueco
        if tablero[0][i-1] == VACIO:
            nuevoTablero=copiar_tablero(tablero)
            coloca_ficha(nuevoTablero,i,quienjuega)
            punt, movs=mejor_puntuacion_2(nuevoTablero,mificha,fichaoponente,sig_jugador,maxturnos-1)
            puntuaciones.append(( punt,[i]+movs ))

    #Máxima puntuación
    mejor_punt=None
    col_mejor_punt=None
    for tup_punt in puntuaciones:
        if mejor_punt is None:
            mejor_punt=tup_punt[0]
            col_mejor_punt=tup_punt[1]
        if mificha == quienjuega:
            if tup_punt[0] > mejor_punt:
                mejor_punt = tup_punt[0]
                col_mejor_punt = tup_punt[1]
        else:
            if tup_punt[0] < mejor_punt:
                mejor_punt = tup_punt[0]
                col_mejor_punt = tup_punt[1]
    return mejor_punt,col_mejor_punt



################ Comienzo del programa ########################
ficha = ROJA
tablero = rellena_matriz_int(NFILAS, NCOLS, 0)
setup_tablero()

#Mientras no haya ganador y quepan más fichas, hacemos una jugada
while ganador(tablero) == None and not tablero_lleno(tablero):
    #Imprimimos tablero en modo texto
    imprime_tablero(tablero)
    try:
        if ficha == ROJA:
            #Comenta la siguiente instrucción si quieres calcular la mejor jugada automáticamente
            col = int(input('Dime la columna donde colocar la ficha ROJA: '))

            #Quita los comentarios del siguiente bloque de código para calcular la mejor jugada automáticamente
            # Cambia mejor_puntuacion por una función de tu elección si deseas probar diferentes alternativas
            #punt, movs = mejor_puntuacion_2(tablero, ROJA, AMARILLA, ROJA, 5)
            #col = movs[0]
            #print("El jugador rojo ha decidido colocar ficha en la columna {} para obtener una puntuación de {} con movimientos {}".format(col, punt, movs))
        else:
            # Comenta la siguiente instrucción si quieres calcular la mejor jugada automáticamente
            col = int(input('Dime la columna donde colocar la ficha AMARILLA: '))

            # Quita los comentarios del siguiente bloque de código para calcular la mejor jugada automáticamente
            #Cambia mejor_puntuacion_2 por una función de tu elección si deseas probar diferentes alternativas
            #punt,movs = mejor_puntuacion_2(tablero, AMARILLA,ROJA, AMARILLA, 5)
            #col=movs[0]
            #print("El jugador amarillo ha decidido colocar ficha en la columna {} para obtener una puntuación de {} con movimientos {}".format(col,punt,movs))
        if 1 <= col <= 7:
            try:
                #Coloca ficha y cambia color para el siguiente turno
                coloca_ficha(tablero, col, ficha, pintar=True)
                if ficha == AMARILLA:
                    ficha = ROJA
                else:
                    ficha = AMARILLA
            except ValueError as e:
                error(e)
        else:
            error('La columna debe ser entre 1 y 7')
    except ValueError as e:
        error('Debe introducir un número, vuelva a intentarlo')


imprime_tablero(tablero)

if ganador(tablero) == None:
    print("Empate")
else:
    if ganador(tablero) == ROJA:
        print('El ganador es la ficha ROJA')
    else:
        print('El ganador es la ficha AMARILLA')