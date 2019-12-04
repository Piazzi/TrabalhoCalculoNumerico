import numpy as np
import matplotlib.pyplot as plt
import math

def criaMatriz(x, ordem):
    shape = (len(x), ordem + 1)
    matrizA = np.zeros(shape)
    matrizA[ : , 0 ] = 1
    for index, value in enumerate (x):
        for n in range (1, ordem +1):
            matrizA[index, n] = value ** n
       

    return matrizA

if __name__ == "__main__":

    x = []
    y = []
    arquivo = open("ex1_dados.txt", "r")
    for linha in arquivo:
        x.append(arquivo.readline().strip().split()[0])
        #y.append(arquivo.readline().strip().split()[0])
    
    print(x)
    print(y)