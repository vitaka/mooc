#Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
def digitos(n):
    if n < 10:
        return 1
    else:
        return 1+ digitos(n//10)

#Escribir una función que reciba un número positivo n y devuelva la suma de dus dígitos.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n%10 + suma_digitos(n//10)


#Escribir una funcion recursiva que encuentre el mayor elemento de una lista.
def mayor(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    mayor_resto=mayor(l[1:])
    if l[0] > mayor_resto:
        return l[0]
    else:
        return mayor_resto


#Escribir una función recursiva que compruebe si una cadena es un palíndromo
def palindromo(s):
    if len(s) <=1:
        return  True
    else:
        if s[0] != s[-1]:
            return False
        else:
            return palindromo(s[1:-1])
