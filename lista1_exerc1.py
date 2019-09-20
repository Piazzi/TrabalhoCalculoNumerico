
from math import *
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
def ln_taylor(n,x):
    fator = x
    soma = 0
    for n in range(1,n+1):
        fator = ((-1)**(n-1)) * (x**n/n)
        soma = soma + fator
    return soma


def lnnegativa_taylor(n,x):
    ''' tentando criar a função que faz ln negativa'''  
    term= -x/(1-x)
    sum = term
    for i in range(2,n+1):
        term = term*x/(1-x)
        sum = sum + term/i
    return sum
   
# -----------------------------------------------------------------------------

def taylor(f, x0, x):
    """
    Calcula uma aproximacao para uma funcao f(x) qualquer usando o
    polinomio de Taylor de grau n em torno de x=x0. A funcao f(x) deve
    ser fornecida como um vetor com os valores da funcao e suas
    derivadas.
    Parametros:
       - f  - vetor com os valores da funcao e suas derivadas no ponto x0
       - x0 - valor do ponto de referencia
       - x  - valor de x aonde se deseja calcular f(x)
       
    Exemplo:
   
    """
    n = len(f)
    if n == 0:
        print("Erro. Devem ser fornecidos os valores de f(x0), f'(x0), ...")
        return None
    h   = x - x0
    fat = 1.0
    termo = 1.0
    resultado = f[0]
    i = 1
    while i < n:
        fat = fat * i
        termo = termo * h
        resultado = resultado + (f[i]*termo)/fat
        i = i + 1
    return resultado


# -----------------------------------------------------------------------------

if __name__ == "__main__":

    print("Polinomios de Taylor\n")

    # Teste 1 - Testa aproximacao para exp(x)
    print("Aproximacao para exp(x)")
    n = 1000
    x = 1
    ap = ln_taylor(n,x)
    ex = np.log(2)
    er = abs(ex-ap)
    print(" Exato = %e" % ex)
    print(" Aprox = %e" % ap)
    print(" Erro  = %e\n" % er)

    x = np.linspace(0,1,10000)
    y = np.log(x)
    #n = 3
    yy = lnnegativa_taylor(n,x-1)
    plt.plot(x,y,label="LN")
    plt.plot(x,yy,label="taylor")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Polinomio de Taylor")
    plt.legend(loc="best")
    plt.show()
    plt.savefig("teste1.png")

    