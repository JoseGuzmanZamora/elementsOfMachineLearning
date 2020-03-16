import numpy as np 
import matplotlib.pyplot as plt 
from scipy import optimize as op

def logistic(x, thetas):
    """
    Computar el resultado de ingresar una serie de 
    columnas con sus respectivos coeficientes a la 
    función logística. 
    """
    multi = np.matmul(x, thetas)
    x = 1 / (1 + np.exp(-multi))
    return x

def cost(thetas, X, Y):
    """ 
    Calcular el costo de un conjunto de hipótesis basado en 
    la cantidad de thetas ingresados.
    """ 
    hips = logistic(X, thetas)
    prefix = - 1 / X.shape[0]
    central = (Y * np.log(hips)) + ((1 - Y) * np.log(1 - hips))
    return prefix * np.sum(central)

def derivative(thetas,X,Y):
    """
    Encontrar la derivada de la función de costo y retornar 
    la suma de todas las hipótesis.
    """
    thetas = thetas.reshape(len(thetas), 1)
    hips = logistic(X, thetas)
    interno = (hips - Y).transpose()
    res = (1 / X.shape[0]) * np.matmul(interno, X).transpose()
    return np.squeeze(res)

def optimizar(x, y, method):
    """
    Encontrar el punto mínimo de los coeficientes para el 
    conjunto de columnas. 
    """
    initial = np.expand_dims(np.asarray([0 for i in range(len(x[0]))]),1)
    return np.expand_dims(op.minimize(cost, initial, args=(x,y),jac=derivative,method=method).x, 1)