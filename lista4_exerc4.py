import lista4_exerc1 as solvers
import lista4_exerc3 as cond
import numpy as np
from numpy import linalg as LA


# Funcao que monta o sistema Hx = b a ser resolvido
# Parâmetro n: ordem da matriz e do vetor
def sistema(n):
    H = np.zeros((n,n))
    b = np.zeros(n)

    for i in range (0, n):
        for j in range(0, n):
            H[i,j] = 1/(i+j+1)
    
    for i in range(0, n):
        b[i] = 1/(1+n+i)

    return H, b
    

# Funcao que calcula o erro cometido por cada metodo
# H = Matriz H
# x = vetor solucao
# b = vetor b 
# n = tamanho
def residuo(H , x ,b, n):
    r = []
    for i in range(0,n):
        for j in range(0,n):
            r.append(H[i][j]*x[j] - b[i])

    return abs(max(r,key=abs))


# Funcao que resolve o sistema de equacoes lineares Ax=b usando
#  o metodo da Eliminacao de Gauss com pivoteamento.
def gaussComPivotamento(A,b):
    n = b.shape[ 0 ]

    # Etapa de eliminacao
    for k in range(0,n-1):
        for i in range(k+1,n):
            print(A)
            if(abs(A[i][k]) < abs([max(i) for i in zip(*A)][k]) ):
                # pega o indice do pivo
                indice = A.argmax(axis=0)
                # troca de linhas
                A[[k,indice[k]]] = A[[indice[k],k]]
            else:
                pass

            if A[i,k] != 0.0:
                m = A[i,k]/A[k,k]
                for j in range(k,n):
                    A[i,j] = A[i, j] - m * A[k,j]
                b[i] = b[i] - m * b[k]
                   
    # Resolve o sistema triangular
    x = solvers.retrosubstituicao( A, b )
    return x

def exemplo():
    A = np.array([[1,1,1],
                  [2,3,5],
                  [4,6,8]])
    b = np.array([[3],[10],[18]])
    return A, b

A, b = exemplo()

print("MATRIZ A: ")
print(gaussComPivotamento(A,b))

# Problem 4,  Letra D
#cond.condMatriz(sistema(5))
#cond.condMatriz(sistema(10))
#cond.condMatriz(sistema(100))
#cond.condMatriz(sistema(1000))

#A, b = sistema(1000)
#print(residuo(A, solvers.gauss(A,b), b, A.shape[0]))


