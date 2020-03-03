import numpy as np 
#import matplotlib.pyplot as plt 

def logistic(x, thetas):
    multi = np.matmul(thetas.transpose(), x)
    return 1 / (1 + np.e ** (-multi))

x = [1,2,6,5,2,1,2,3,5]
x2 = [1,2,6,5,2,1,2,3,5]
xc = [0,0,0,0,0,0,0,0,0]
thetas = np.asarray([1,1,1])

junto = np.asarray(np.vstack([xc,x,x2]))
print(logistic(junto, thetas))

def cost(X,Y,thetas, l):
    """ 
    Calcular el costo de un conjunto de hipótesis basado en 
    la cantidad de thetas ingresados.
    """
    hipos = logistic(X, thetas)
    regular = (l / (2 * X.shape[0]))
    return (np.sum(np.power(hipos - Y, 2)) / (2 * X.shape[0])
            + (regular * np.sum(thetas ** 2)))


def derivative(X,Y,thetas):
    """
    Encontrar la derivada de la función de costo y retornar 
    la suma de todas las hipótesis.
    """
    hips = logistic(X, thetas)
    interno = (hips - Y).transpose()
    return np.matmul(interno, X).transpose()

def gradient_descent(X, Y, thetas, a, it, delta, l):
    """
    Aplica descenso del gradiente en base a un dataset y thetas iniciales.

    Params:
    - X : valores de x con columna de 1s agregada al inicio
    - Y : valores de entrenamiento
    - a : learning rate
    - it : cantidad de iteraciones
    - delta : cambio mínimo para parar las iteraciones
    """
    procesado = np.asarray(thetas, dtype='float64').reshape(len(thetas),1)
    m, _ = X.shape
    trace = []
    for i in range(it):
        costo1 = cost(X,Y,procesado,l)
        procesado = (procesado * (1 - ((a * l)/m))) - (a /
         m) * derivative(X,Y,procesado)
        costo = cost(X,Y,procesado,l)
        trace.append((i, procesado, costo))
        if np.abs(costo1 - costo) <= delta:
            print("no")
            print(i)
            break
    return trace

