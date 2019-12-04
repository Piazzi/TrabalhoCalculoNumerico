import numpy as np
import matplotlib.pyplot as plt
import math

def substituicao(A, b):
    """
    Uso: x = substituicao(A,b)    
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes sucessivas, ou seja, assume-se que A
    e uma matriz triangular inferior.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += A[i,j] * x[j]
        x[i] = ( b[i] - soma ) / A[ i, i ]
    
    return np.matrix(x).transpose()

def criaMatriz(x):
    shape = (len(x), 3)
    matrizA = np.zeros(shape)
    matrizA[ : , 0 ] = 1
    for index, value in enumerate (x):
        matrizA[index, 1] = value
        matrizA[index, 2] = value ** 2

    return matrizA
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
	
def cholesky(A):
    """
    Uso: G = cholesky(A)
    
    Essa funcao gera a matriz G da decomposicao de Cholesky
    e a armazena na propria matriz A.
    """
    n = A.shape[0]

    # etapa de eliminacao
    for j in range(0,n):
        soma = 0
        for k in range(0,j):
            soma += A[j,k]*A[j,k]

        try: 
            A[j,j] = math.sqrt(A[j,j] - soma)
        except ValueError:
            print("A matriz nao eh positiva definida.")
                
        for i in range(j+1,n):
            soma = 0
            for k in range(0,j):
                soma += A[i,k]*A[j,k]
            A[i,j] = ( A[i,j] - soma ) / A[j,j]

    # zera a parte triangular superior
    for k in range(1,n):
        A[0:k,k] = 0.0

    return A

# -----------------------------------------------------------------------------

def solveCholesky(G,b):
    """
    Uso: x = choleskySolve(G,b)
    Resolve o sistema Ax=B usando a decomposicao de Cholesky A = G G^T,
    sendo que G foi obtida atraves do uso da funcao cholesky(A) na
    matriz do sistema A.
    
    G deve ser triangular inferior.
    """
    n = len(b)    
    # substituicao - resolve Gy = b
    y = substituicao(G,b)    
    # retrosubstituicao - resolve G^T x = y
    Gt = G.T
    x = retrosubstituicao(Gt,y)
    return x
                    
# -----------------------------------------------------------------------------

 
if __name__ == "__main__":

    x = [-1, 0, 1, 2]
    y = [0, -1, 0, 7]
    A = criaMatriz(x)
    ATransposta = np.transpose(A)
    M = ATransposta.dot(A)
   
    F = ATransposta.dot(y)
    G = cholesky(M)
    c = solveCholesky(G, F)
    x_g = np.linspace(-1, 2 , 10000)
    y_g = [ ]
    print(A)
    print(ATransposta)
    print(c)
    for value in x_g :
        y_g.append(g(c, value))
        plt.plot(x_g, y_g)
        plt.scatter(x, y, color='blue')
        plt.show()


