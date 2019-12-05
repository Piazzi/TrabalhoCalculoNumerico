import numpy as np
import matplotlib.pyplot as plt
import math
import lista6_exerc1 as solvers

def criaMatriz(x, ordem):
    matrizA = np.zeros((len(x), ordem + 1))
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
        linha[0] = linha[0].replace(';','').replace(',','.')
        linha[1] = linha[1].replace(',', '.')
        x.append(float(linha[0]))
        y.append(float(linha[1]))
    
    
    
    return x,y

def g(c,x):
    y = 0
    for(index,value) in enumerate(c):
        y += c.item(index)*x**index
    
    return y

if __name__ == "__main__":

    x, y = leituraArquivo()
    A = criaMatriz(x, 1)
    ATransposta = np.transpose(A)
    M = ATransposta.dot(A)
   
   
   
    F = ATransposta.dot(y)
    G = solvers.cholesky(M)
    c = solvers.solveCholesky(G, F)
    print(c)

    x_g = np.linspace(-1,  6, 10000)
    y_g = [ ]
    
    for value in x_g :
        y_g.append(g(c, value))

    plt.plot(x_g, y_g)
    plt.scatter(x, y, color='green')
    plt.show()