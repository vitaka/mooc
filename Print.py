from sys import stdout, stderr


print('Hola', 'Adiós', 'Pepe', end=" -> ")
cad = "Hola"
real = 3.2
num = 5
print(cad, real, num, end="|")
print(end="<<<<>>>>")
print("Adiós")
print("Valor1", "valor2", 3.5, num, sep=",", file=stderr)
