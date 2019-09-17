import numpy as np

# Lista 2 - Problema 1
# Tipos de váriaveis disponíveis no pacote numpy: https://docs.scipy.org/doc/numpy/user/basics.types.html?highlight=float32#array-types-and-conversions-between-types

def divisao(n):
    cont = 0
    while(1+n != 1):
        n = n/2
        cont = cont+1
        print(n)
    print("Número de Iterações", cont)
    return n

x = np.single(0.5) # 0.5 em precisão simples
y = np.double(0.5) # 0.5 em precisão dupla

print("Precisão simples: ")
x = divisao(x)
print("----------------------------------------------")
print("Precisão dupla: ")
y = divisao(y)
print("Precisão simples: ", x, "X Precisão dupla: ", y)