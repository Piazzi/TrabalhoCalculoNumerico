import numpy as np
from numpy import linalg

# ----------------- MÉTODO DE GAUSS-SEIDEL ----------------------
# A = Matriz
# b = vetor
# tol = tolerancia
# N = número máximo de iterações
def gauss_seidel(A,b,x0,tol,N):
    
    ordem = np.shape(A)[0]
    if(criterio_de_sassenfeld(A, ordem)):
        print("O critério de sassenfeld foi satisfeito")
    else:
        return "O critério de sassenfeld não foi satisfeito, insira outra matriz"
    i = 0
    while(i < N):
        i+=1
        for j in range(0, ordem):         
            d = b[j]                   
            
            for i in range(0, ordem):      
                if(j != i): 
                    d-=A[j][i] * x0[i] 
            x0[j] = d / A[j][j] 
        # returning our updated solution  
        if (np.linalg.norm(x0,np.inf) < tol):      
            return x0,i     
    print('Numero de iteracoes excedido.')
    

def criterio_de_sassenfeld(A,ordem):
    somatorio = 0
    # vetor de betas
    betas = np.zeros(ordem)

    for i in range (0,ordem):
        for j in range (0, ordem):
            if(i != j):
                if(i == 0):
                    somatorio = somatorio + A[i][j]/A[i][i]
                if(betas[j] != 0):
                    somatorio = somatorio + A[i][j]/A[i][i]*betas[j]

        betas[i] = somatorio
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
    print("Solucao e numero de iteracoes: ", gauss_seidel(A1,b1, [0,0,0],10,10))

    A1,b1 = exemplo1()
    print("MATRIZ: ")
    print(A1)
    print("VETOR: ")
    print(b1)
    print("Solucao e numero de iteracoes: ", gauss_seidel(A1,b1, [0,0,0],10,10))


    
