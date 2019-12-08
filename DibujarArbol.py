import turtle


def pintar_ramas(longitud, reducir, angulo, nivel):
    if nivel <= 0 or longitud <= 0:
        return
    turtle.forward(longitud)
    turtle.left(angulo)
    pintar_ramas(longitud - reducir, reducir, angulo, nivel - 1)
    turtle.right(angulo * 2)
    pintar_ramas(longitud - reducir, reducir, angulo, nivel - 1)
    turtle.left(angulo)
    turtle.backward(longitud)


def pintar_arbol(x, y, tronco, reducir, angulo, nivel):
    # Posiciono la tortuga
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # Pinto el tronco
    turtle.setheading(90)
    turtle.forward(tronco)
    turtle.right(angulo)
    pintar_ramas(tronco - reducir, reducir, angulo, nivel - 1)
    turtle.left(angulo)
    turtle.backward(tronco)


turtle.setup(600, 600)

pintar_arbol(-200, -300, 100, 5, 20, 7)

turtle.exitonclick()