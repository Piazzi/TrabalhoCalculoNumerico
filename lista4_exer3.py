import numpy as np
from numpy import linalg

def condMatriz(A):
    print("Matriz A: \n", A)
    inversa = np.linalg.inv(A)
    print("Inversa de A: \n", inversa)
    cond = np.linalg.norm(A, 2)* np.linalg.norm(inversa, 2) 
    print("Condicionamento :", cond)


A = np.array([[5,-2],
             [-2,4]])

condMatriz(A)