import numpy as np 
import matplotlib.pyplot as plt 

# FUNCION DE COSTO 
'''
Ingresa un X con una fila de 1s para hacer la multiplicación en el futuro con Xi 
Entra un Y con los valores que tenemos como predicción 

J(z0,z1) = 1 / 2m * sumatoria de 1 a m (donde m es la cantidad de datos) 

(H(xi) - Yi) ^ 2 

Esta definición indica que tiene que ingresar un arreglo de tetas 
'''

def cost(X,Y,thetas):
    hipos = np.matmul(X, thetas)
    return np.sum(np.power(hipos - Y, 2)) / (2 * X.shape[0])

# FUNCION DE DERIVADA 

'''
Esta se puede expresar de la siguiente manera:
dJ(theta)/dtheta0 = 1/m * sum de 1 a m de (H(thetas) - Yi) * Xi
 '''

def derivative(X,Y,thetas):
    hips = np.matmul(X, thetas)
    interno = (hips - Y).transpose()
    return (np.matmul(interno, X) / X.shape[0]).transpose()


# RANDOM DATASET 
# y = 0.6x + 3
x = np.asarray([np.random.randint(250) for i in range(100)]).reshape(100,1)
ys = np.asarray([(0.6 * i + (3 * np.random.randint(10))) for i in x]).reshape(100,1)

# recibo la data 
xs = np.hstack((np.ones(100).reshape(100,1), x))

thetas = [9,4]

procesado = np.asarray(thetas).reshape(len(thetas),1)
print(cost(xs,ys,procesado))
print(derivative(xs,ys,procesado))



