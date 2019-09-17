import math
import numpy as np

# Lista 2 - Problema 2
# Representacao de uma equacao quadratica: ax^2 + bx + c = 0

def bhaskara(a, b, c):
    delta = b**2 - (4*a*c)
    if(a == 0):
        x1 = -c/b
        print("x1: ",x1)
        return x1

    x1 = (-b - math.sqrt(delta))/(2*a) 
    x2 = (-b + math.sqrt(delta))/(2*a)

    print("x1: ", x1)
    print("x2: ", x2)
    raizes = [x1,x2]
    return raizes

print("Para a equação 6x^2 + 5x - 4 foi obtido as raizes: ")
bhaskara(6,5,-4)

print("Para a equação 6*10^30x^2 + 5*10^30x + 4*10^30 foi obtido as raizes: ")
bhaskara(6*(10^30),5*(10^30),-4*(10^30))

print("Para a equação x + 1 foi obtido as raizes: ")
bhaskara(0,1,1)

print("Para a equação x^2  - 10*^5x + 1 foi obtido as raizes: ")
bhaskara(1,-10^5,1)

print("Para a equação x^2  - 4 + 3.999999 foi obtido as raizes: ")
bhaskara(1,-4,3.999999)

print("Para a equação 10^-30x^2  - 10*^30x + 10^30 foi obtido as raizes: ")
bhaskara(10*(10^-30),-10*(10^-30),10*(10^-30))

