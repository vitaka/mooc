def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(2, 101):
    if es_primo(i):
        print(i)
