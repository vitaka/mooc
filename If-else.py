def mayor_2_nums(num1, num2):
    return num1 if num1 > num2 else num2


def mayor_3_nums(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        return num3
    else:
        if num2 > num3:
            return num2
        return num3


num1 = int(input('Introduce un número: '))
num2 = int(input('Introduce otro número: '))
num3 = int(input('Introduce otro número: '))

mayor = mayor_2_nums(num1, num2)
print('El número mayor es', mayor)
mayor = mayor_3_nums(num1, num2, num3)
print('El número mayor es', mayor)
