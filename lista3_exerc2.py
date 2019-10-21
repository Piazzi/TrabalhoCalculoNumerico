import numpy as np
import math
import matplotlib.pyplot as plt

def pontofixo(phi,x,tol=1e-8,maxit=100):
    """
    Essa funcao implementa o metodo do Ponto Fixo. Recebe como
    parametros, a funcao de iteracao phi, uma aproximacao inicial x e
    ainda a precisao tol e numero maximo de iteracoes maxit.
    """
    print("\nMETODO DO PONTO FIXO")
    x0 = x
    for k in range(maxit):
        x1 = phi(x0)

        print(" %d %e %e" % ( k, x1, abs(x1-x0) ))

        if (abs( x1 - x0 ) <= tol):
            plt.plot(x1)
            return x1
        x0 = x1

    print("Numero maximo de iteracoes excedido")
    return None

### f(x) = cos(x) +  1%(1+e^-2x)

def letraA(x0):
    return np.arccos(-1/(1+np.math.e**(-2*x0)))

def letraB(x0):
    return 0.5*math.log(-1/(1+(1/np.cos(x0))))

print(pontofixo(letraA, 3,0,100))
print('-----------------------------')


plt.plot(pontofixo(letraA, 3,0,100),label="exp")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Ponto Fixo")
plt.legend(loc="best")
plt.show()
plt.savefig("teste1.png")