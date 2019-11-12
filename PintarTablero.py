import turtle as t


def square(x, y, size, color='black', fill=None):
    rectangle(x, y, size, size, color, fill)


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


def circle(x, y, size, color='black', fill=None):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    if fill != None:
        t.fillcolor(fill)
        t.begin_fill()
    t.circle(size)
    t.end_fill()


def col_nums():
    x = COL_SIZE // 2
    for i in range(1, 8):
        t.penup()
        t.goto(x, COL_SIZE + (COL_SIZE // 10))
        t.pendown()
        t.write(i, align='center', font=('Arial', COL_SIZE - (COL_SIZE // 10), 'normal'))
        x = COL_SIZE * i + COL_SIZE // 2

def board(size):
    col_nums()
    rectangle(0, COL_SIZE, size, size - COL_SIZE, 'black', 'green')
    for i in range(7):
        for j in range(6):
            ficha(i + 1, j + 1, 'white')


def ficha(col, row, color):
    circle_radius = (COL_SIZE - COL_SIZE // 10) // 2
    x = COL_SIZE // 2 + (col - 1) * COL_SIZE
    y = COL_SIZE + (row - 1) * COL_SIZE + COL_SIZE // 20
    circle(x, y, circle_radius, color, color)


BOARD_SIZE = 700
COL_SIZE = BOARD_SIZE // 7

t.setup(BOARD_SIZE, BOARD_SIZE)
#  t.screensize(BOARD_SIZE, BOARD_SIZE)
t.setworldcoordinates(0, BOARD_SIZE + 10, BOARD_SIZE + 10, -10)
t.speed(0)
# t.showturtle()
t.hideturtle()
t.shape('turtle')

board(BOARD_SIZE)
ficha(4, 6, 'red')
ficha(3, 6, 'blue')
ficha(4, 5, 'red')
ficha(5, 6, 'blue')
# rectangle(0, 0, 500, 400, 'black', 'green')
# square(50, 100, 50, 'red', 'yellow')
# circle(300, 50, 26, 'red', 'black')

t.exitonclick()