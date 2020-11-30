import turtle as t

BOARD_SIZE = 700
COL_SIZE = BOARD_SIZE // 7

### Dibuja un cuadrado ###
def square(x, y, size, color='black', fill=None):
    rectangle(x, y, size, size, color, fill)

### Dibuja un rectángulo ###
def rectangle(x, y, sizex, sizey, color='black', fill=None):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    if fill != None:
        t.fillcolor(fill)
        t.begin_fill()
    for i in range(4):
        t.forward(sizex if i % 2 == 0 else sizey)
        t.left(90)
    t.end_fill()

## Dibuja un círculo ##
def circle(x, y, size, color='black', fill=None):
    t.penup()
    t.goto(x, y)
    #t.showturtle()
    t.pendown()
    t.pencolor(color)
    if fill != None:
        t.fillcolor(fill)
        t.begin_fill()
    t.circle(size)
    t.end_fill()
    #t.hideturtle()

### Dibuja números de columna ####
def col_nums():
    x = COL_SIZE // 2
    for i in range(1, 8):
        t.penup()
        t.goto(x, COL_SIZE + (COL_SIZE // 10))
        t.pendown()
        t.write(i, align='center', font=('Arial', COL_SIZE - (COL_SIZE // 10), 'normal'))
        x = COL_SIZE * i + COL_SIZE // 2

### Dibuja el tablero inicial, con todas posiciones vacías ###
def board(size):
    col_nums()
    rectangle(0, COL_SIZE, size, size - COL_SIZE, 'black', 'blue')
    for i in range(7):
        for j in range(6):
            pinta_ficha(i + 1, j + 1, 'white')


### Dibuja una ficha de color "color" en la columna "col" y la fila "row"
def pinta_ficha(col, row, color):
    circle_radius = (COL_SIZE - COL_SIZE // 10) // 2
    x = COL_SIZE // 2 + (col - 1) * COL_SIZE
    y = COL_SIZE + (row - 1) * COL_SIZE + COL_SIZE // 20
    circle(x, y, circle_radius, color, color)

## Inicializa el juego: configura turtle y dibuja un tablero vacío
def setup_tablero():
    t.setup(BOARD_SIZE, BOARD_SIZE)
    t.setworldcoordinates(0, BOARD_SIZE , BOARD_SIZE, 0)
    t.speed(0)
    t.hideturtle()
    t.shape('turtle')
    board(BOARD_SIZE)


