import numpy as np
from numpy import linalg

# ----------------- MÉTODO DE JACOBI ----------------------
# A = Matriz
# b = vetor
# tol = critério de parada
# N = número máximo de iterações
def jacobi(A,b,x0,tol,N):
    
     # Pega a ordem da matriz
    ordem =np.shape(A)[0]
    if(criterio_das_linhas(A, ordem)):
        print("O critério das linhas foi satisfeito")
    else:
        return "O critério das linhas não foi satisfeito, insira outra matriz"

    x = np.zeros(ordem)
    # Contador de iterações
    i = 0
    while (i < N):
        i += 1
        for i in np.arange(ordem):
            x[i] = b[i]
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,ordem))):
                x[i] -= A[i,j]*x0[j]
            x[i] /= A[i,i]

        if (np.linalg.norm(x-x0,np.inf) < tol):
            return x,i

        x0 = np.copy(x)
    print('Numero de iteracoes excedido.')

def criterio_das_linhas(A, ordem):
    somatorio = 0
    for i in range(0, ordem):
        for j in range(0, ordem):
            if(i != j):
                somatorio = somatorio + A[i][j]/A[i][i]
    
        if(somatorio >= 1):
            return 0
        somatorio = 0    
    return 1


def exemplo1():
    A = np.array([[5,1,1],
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
    A1,b1 = exemplo2()    
    print("MATRIZ: ")
    print(A1)
    print("VETOR: ")
    print(b1)
    print("Solucao e numero de iteracoes: ", jacobi(A1,b1, [0,0,0],10,10))

    A1,b1 = exemplo1()
    print("MATRIZ: ")
    print(A1)
    print("VETOR: ")
    print(b1)
    print("Solucao e numero de iteracoes: ", jacobi(A1,b1, [0,0,0],10,10))

