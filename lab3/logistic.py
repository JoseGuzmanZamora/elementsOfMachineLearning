import numpy as np 
import matplotlib.pyplot as plt 

def logistic(x, thetas):
    multi = np.matmul(x, thetas)
    return 1 / (1 + np.e ** (-multi))

def cost(X,Y,thetas):
    """ 
    Calcular el costo de un conjunto de hipótesis basado en 
    la cantidad de thetas ingresados.
    """
    hips = logistic(X, thetas)
    prefix = - 1 / X.shape[0]
    central = (Y * np.log(hips)) + ((1 - Y) * np.log(1 - hips))
    return prefix * np.sum(central)

def derivative(X,Y,thetas):
    """
    Encontrar la derivada de la función de costo y retornar 
    la suma de todas las hipótesis.
    """
    hips = logistic(X, thetas)
    interno = (hips - Y).transpose()
    return (1 / X.shape[0]) * np.matmul(interno, X).transpose()

def gradient_descent(X, Y, thetas, a, it):
    """
    Aplica descenso del gradiente en base a un dataset y thetas iniciales.

    Params:
    - X : valores de x con columna de 1s agregada al inicio
    - Y : valores de entrenamiento
    - a : learning rate
    - it : cantidad de iteraciones
    """
    trace = []
    for i in range(it):
        costo1 = cost(X,Y,thetas)
        thetas -= a * derivative(X,Y,thetas)
        costo = cost(X,Y,thetas)
        trace.append((thetas, costo))
    return trace


'''xc = [1,1,1,1,1,1,1,1,1]
x = [1,2,6,5,2,1,2,3,5]
x2 = [1,2,4,9,2,1,2,3,5]
junto = np.vstack([xc,x,x2]).transpose()
y = [0,1,1,0,0,1,0,1,0]
y = np.asarray(y).reshape(len(y), 1)
thetas = [1,1,1]
thetas = np.asarray(thetas, dtype='float64').reshape(len(thetas), 1)
# IMPORTANTE AHORITA TODO YA ESTA  EN FORMA DE COLUMNA... 

# X, Y, THETAS TIENEN QUE SER FORMA COLUMNA'''
