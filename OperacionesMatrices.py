from utils import imprime_matriz, int_matriz_random
import numpy as np


def suma_matrices(A, B):
    M = []
    if len(B) != len(A):
        raise ValueError('La matriz A tiene que tener las mismas dimensiones que la B')
    for i in range(len(A)):
        row = []
        if len(A[i]) != len(B[i]):
            raise ValueError('La matriz A tiene que tener las mismas dimensiones que la B')
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        M.append(row)
    return M


def mult_matrices(A, B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[i])):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)
    return C

# imprime_matriz(int_matriz_random(6, 7, 1, 10))
A = int_matriz_random(4, 4, 0, 10)
B = int_matriz_random(4, 4, 0, 10)
imprime_matriz(A)
print()
imprime_matriz(B)
print()
#imprime_matriz(suma_matrices(A, B))
print("Multiplicación AxB")
C = mult_matrices(A, B)
imprime_matriz(C)
print("Multiplicación usando numpy")
A = np.array(A)
B = np.array(B)
C = A.dot(B)
print(C)

