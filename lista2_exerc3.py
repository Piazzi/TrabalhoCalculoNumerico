import numpy as np
import math
import matplotlib.pyplot as plt

# Lista 2 - Problema 3

def derivada(x, h):
  return  (math.sin(x+h) - math.sin(x)) / h


print("Derivada encontrada pelo método: ", derivada(1,1))
print("Derivada exata: ", math.cos(1))
print("Erro: ", math.cos(1) - derivada(1,1))

"""
for i in range(1,5):
    div = 2
    erro = math.cos(1) - derivada(1, 1/div)
    plt.plot([erro,2 ,3])
    div = div*2
"""

erro1 = math.cos(1) - derivada(1, 1/2)
erro2 = math.cos(1) - derivada(1, 1/4)
erro3 = math.cos(1) - derivada(1, 1/8)
erro4 = math.cos(1) - derivada(1, 1/16)
erro5 = math.cos(1) - derivada(1, 1/32)
erro6 = math.cos(1) - derivada(1, 1/64)
erro7 = math.cos(1) - derivada(1, 1/128)
erro8 = math.cos(1) - derivada(1, 1/256)
erro9 = math.cos(1) - derivada(1, 1/512)
erro10 = math.cos(1) - derivada(1, 1/1024)


plt.plot([erro1,erro2,erro3,erro4,erro5])
plt.ylabel('Log')
plt.yscale('log')
plt.title('log')
plt.xlabel('Erro')
plt.grid(True)
plt.show()
plt.savefig("log.png")