import turtle

# Configura el tamaño de la ventana
turtle.setup(800,600)
#Hace que las coordenadas 0,0 estén en la esquina inferior izquierda de la pantalla, en vez de en el centro
turtle.setworldcoordinates(0,0,800,600)

#Muestra la tortuga
turtle.showturtle()

#Avanzamos 200 puntos sin dibujar
turtle.penup()
turtle.forward(200)

#Avanzamos 100 puntos dibujando y nos guardamos la posición
turtle.pendown()
turtle.forward(100)
posicion=turtle.pos()
#Avanzamos 300 puntos dibujando
turtle.forward(300)

#Volvemos a la posición anterior, sin dibujar
turtle.penup()
turtle.goto(posicion)

#giramos 90 grados en el sentido inverso de las agujas del reloj para mirar hacia arriba y dibujamos una línea
turtle.left(90)
turtle.pendown()
turtle.forward(500)

# Giramos 90 grados en el sentido de las agujas del reloj para mirar hacia la derecha y dibujamos una línea
turtle.right(90)
turtle.forward(200)

# Giramos 90 grados en el sentido de las agujas del reloj para mirar hacia abajo y dibujamos una línea
turtle.right(90)
turtle.forward(100)

#Dibujamos un cuadrado con relleno rojo
turtle.fillcolor('red')
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()