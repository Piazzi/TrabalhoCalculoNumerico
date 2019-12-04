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

def leituraArquivo():
    arquivo = open("ex1_dados.txt", "r")
    x = []
    y = []
    for linhas in arquivo:
        linha = linhas.split()
        x.append(linha[0])
        y.append(linha[1])
    
    return x,y

if __name__ == "__main__":

    x, y = leituraArquivo()
        
    
    print(x)
    print(y)