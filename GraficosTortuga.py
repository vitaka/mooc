import turtle as t

def square(x, y, size, color, fill=None):
    rectangle(x, y, size, size, color, fill)


def rectangle(x, y, width, height, color, fill=None):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    if fill != None:
        t.begin_fill()
        t.fillcolor(fill)
    for i in range(4):
        if i % 2 == 0:
            t.forward(width)
        else:
            t.forward(height)
        t.right(90)
    if fill != None:
        t.end_fill()


def geometrica(x, y, edges, size, color, fill=None):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    if fill != None:
        t.begin_fill()
        t.fillcolor(fill)
    for i in range(edges):
        t.forward(size)
        t.right(360 // edges)
    if fill != None:
        t.end_fill()


t.setup(500, 500)
t.speed(1)
t.bgcolor('orange')
t.showturtle()
t.shape('turtle')
geometrica(100, -100, 8, 20, 'magenta', fill='purple')
t.left(90)
square(0,0, 50, 'green')
rectangle(100, 100, 25, 50, 'blue', 'pink')
geometrica(100, -100, 6, 20, 'grey')

t.forward(125)
t.right(45)
t.forward(200)
t.pencolor('red')
t.backward(125)
t.penup()
t.goto(-125, 50)
t.fillcolor('yellow')
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()
t.write('Hola mundo', font=('Arial', 20, 'normal'))

t.exitonclick()