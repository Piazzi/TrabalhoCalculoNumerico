# coding=utf-8
import numpy as np
from copy import deepcopy
import sys


def inversa(A):
    shape = A.shape

    if shape[0] != shape[1]:
        print ("Matriz não é quadrada, insira uma matriz quadrada")
        return None

    if(invertivel(A) == 0):
        return None

    I = matriz_identidade(shape[0])
    decompLU(A)

    M = np.zeros(shape)

    for index in enumerate(A):
        b = np.zeros((shape[0],shape[0]))
        b[index] = 1

        x = solveLU(A, b)
        M[:, index] = x[:]

    print("inversa: ", M)
    if(np.matmul(A,M) == I):
        print("A matriz inversa encontrada esta correta")
        
    return M


def decompLU(A):
    """
    Uso: decompLU(A)
   
    Essa funcao decompoe a matriz de coeficientes A no produto LU
    e armazena o resultado na propria matriz A.
    """
    n = A.shape[ 0 ]
    # Etapa de eliminacao
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                m = A[i,k]/A[k,k]
                A[i,k] = m
                for j in range(k+1,n):
                    A[i,j] = A[i, j] - m * A[k,j]

# -----------------------------------------------------------------------------

def solveLU(A,b):    
    """
    Uso: x = solveLU(A,b)
    Essa funcao recebe uma matriz A = LU, a qual ja foi fatorada
    em L e U e resolve o sistemas de equacoes y = np.zeros(n)Ax = b e retorna
    o vetor solucao x.
   
    Etapas:
      - a matriz A deve ser [A]=[L/U]
      - b eh o vetor do lado direito
      - resolve Ly = b
      - resolve Ux = y
      - retorna a solucao em x
    """
    n = len(A)
    x = np.zeros(n)
    y = np.zeros(n)
   
    # substituicao
    y[0] = b[0]
    for k in range(1,n):
        y[k] = b[k] - np.dot(A[k,0:k], y[0:k])

    # retrosubstituicao
    for k in range(n-1,-1,-1):
        x[k] = (y[k] - np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]

    return x

# -----------------------------------------------------------------------------
   
def gauss(A,b):
    """
    Uso: x = gauss(A,b)
    Essa funcao resolve o sistema de equacoes lineares Ax=b usando
    o metodo da Eliminacao de Gauss sem pivoteamento.
    """
    n = b.shape[ 0 ]
    # Etapa de eliminacao
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                m = A[i,k]/A[k,k]
                for j in range(k,n):
                    A[i,j] = A[i, j] - m * A[k,j]
                b[i] = b[i] - m * b[k]
                   
    # Resolve o sistema triangular
    x = retrosubstituicao( A, b )
    return x
# -----------------------------------------------------------------------------

def retrosubstituicao(A,b):
    """
    Uso: x = retrosubstituicao(A,b)
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes retroativas, ou seja, assume-se que A
    e uma matriz triangular superior.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma += A[i,j] * x[j]
        x[i] = (b[i] - soma)/A[i,i]

    return np.matrix(x).transpose()

# -----------------------------------------------------------------------------

# A matriz é invertivel se o determinante dela é diferente de 0
# função que determina se uma matriz A é inversivel ou não    
def invertivel(A):
    resultado = 0 if np.linalg.det(A) == 0 else 1
    if(resultado):
        print("A matriz é inversivel")
        return 1
    else:
        print("A matriz não é inversivel")
        return 0

# -----------------------------------------------------------------------------
   
# função que retorna uma matriz identidade para determinada ordem
def matriz_identidade(ordem):
    I = np.zeros((ordem,ordem))
    for i in range(0, ordem):
        for j in range(0, ordem):
            if(i == j):
                I[i,j] = 1
        
    print(I)
    return I




def exemplo1():
    A = np.array([[5.,1,1],
                  [3,4,1],
                  [3,3,6]])
    b = np.array([[5.],[6],[0]])
    return A, b

def exemplo2():
    A = np.array([[4,0.24,-0.08],
                  [0.09,3,-0.15],
                  [0.04,-0.08,4]])
    b = np.array([[8.],[9],[20]])
    return A, b    

# -----------------------------------------------------------------------------

if __name__ == "__main__":

    #
    # Exemplo 1
    #

    #print("\n\nEXEMPLO 1\n\n")
    A1,b1 = exemplo1()    
    print(A1)
    #print(b1)
    #x1 = gauss(A1,b1)
    #print("Solucao")
    #print(x1)
    #print(A1)
    #print(b1)


    #
    # Exemplo 2 (LU,Cholesky)
    #
    #print("\n\nEXEMPLO 2\n\n")
    #A2,b2 = exemplo1()
    #decompLU(A2)
    #print("Fatores L e U")
    #print(A2)
    #x2 = solveLU(A2,b2)
    #print("Solucao")
    #print(x2)
   
    inversa(A1)
