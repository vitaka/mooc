import turtle


def curva_koch(longitud, level):
    if int(longitud) == 0:
        raise ValueError('El nivel es demasiado alto o la longitud es demasiado pequeña.')
    if level == 0:
        turtle.forward(longitud)
    else:
        curva_koch(longitud / 3, level - 1)
        turtle.left(60)
        curva_koch(longitud / 3, level - 1)
        turtle.left(-120)
        curva_koch(longitud / 3, level -1)
        turtle.left(60)
        curva_koch(longitud / 3, level -1)


def dibuja_koch(x, y, longitud, levels):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    for i in range(3):
        curva_koch(longitud,levels)
        turtle.right(120)


turtle.setup(600, 600)
turtle.speed(0)

dibuja_koch(-200, 100, 400, 5)

turtle.exitonclick()