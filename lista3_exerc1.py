"""
Exemplo de funcao para aproximar exp(x) usando polinomio de Taylor
Calculo Numerico, Turma X, DCC, UFJF, 2019
Bernardo M. Rocha
"""

from pylab import *
from math import acos,pi
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# lISTA 3 - PROBLEMA 1
#------------------------------------------------------------------------------

def vanDerWalls(v):
    # (p + a/v**2)*(v-b) = R*T
    # (p + a/v**2)*(v-b) - R*T = 0
    a = 3.592
    b = 0.04267
    R = 0.082054
    T = 300
    p = 1
    return (p + a/v**2)*(v-b) - R*T

# -----------------------------------------------------------------------------
# Metodos
# -----------------------------------------------------------------------------

def bisecao(f,a,b,tol=1e-8,maxit=100000000):
    """
    Essa funcao implementa o metodo da Biseccao que encontra uma raiz da 
    funcao f no intervalo [a,b] com uma precisao tal que |f(x)| < tol.
    """
    print("\nMETODO DA BISECAO")
    if (f(a)*f(b) > 0):
        print("Nao ha garantias de que existe raiz nesse intervalo.")
        return None
    x = a
    k = 0
    for k in range(maxit):    
        x = (a+b)/2
        print("%d %e %e" % (k,x,f(x)))

        if (abs(f(x)) < tol):
            return x
        
        if(f(a)*f(x) < 0):
            b = x
        else:
            a = x           
        k = k + 1       
    return x

# -----------------------------------------------------------------------------

def pontofixo(phi,x,tol=1e-8,maxit=100):
    """
    Essa funcao implementa o metodo do Ponto Fixo. Recebe como
    parametros a funcao f que se deseja encontrar a raiz, a
    funcao de iteracao phi, uma aproximacao inicial x e
    ainda a precisao tol e numero maximo de iteracoes maxit.
    """
    print("\nMETODO DO PONTO FIXO")
    x0 = x
    for k in range(maxit):
        x1 = phi(x0)

        print(" %d %e %e" % ( k, x1, abs(x1-x0) ))

        if (abs( x1 - x0 ) <= tol):
            return x1
        x0 = x1

    print("Numero maximo de iteracoes excedido")
    return None

# -----------------------------------------------------------------------------

def newton(f,df,x0,tol=1.0e-8,maxit=100):

    print("\nMETODO DE NEWTON")

    for k in range(1,maxit):
        x1  = x0 - f(x0)/df(x0)
        err = abs(x1 - x0)

        print(" %d  %e  %e  %e" % (k, x1, f(x1), err) )

        if (err < tol):
            return x1

        x0 = x1

    print("Numero maximo de iteracoes excedido.")
    return None    

# -----------------------------------------------------------------------------
       
if __name__ == "__main__":

  resultado = bisecao(vanDerWalls, 0.0001, 100, 0.0000001,100)
  print(resultado)