import numpy as np
import math

def ln_taylor1m(n, x):
    somatorio = 0
    for n in range (1, n+1):
        somatorio = somatorio - (x**n)/n
    return somatorio

def ln_taylor(n,x):
    somatorio = 0
    for n in range (1, n+1):
        somatorio = somatorio + abs((((-1)**(n+1)) + 1))*(x**n)/n
    return somatorio
    

resultado = ln_taylor(3,1)
print("Resultado: ", resultado)