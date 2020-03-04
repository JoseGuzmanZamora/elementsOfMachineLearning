import numpy as np 


arreglo = [np.random.randint(1,4) for i in range(10)]

def separa(arreglo, valor):
    return [1 if i == valor else 0 for i in arreglo]

def separa_mejor(arreglo, valor):
    return (arreglo == valor) * 1

print(arreglo)
print(separa(arreglo, 1))
print(separa(arreglo, 2))
print(separa(arreglo, 3))