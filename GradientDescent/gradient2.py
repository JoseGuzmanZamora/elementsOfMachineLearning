# Gradient Descent Vectorial

import numpy as np 
import matplotlib.pyplot as plt

def derivada(data, theta, alpha):
    data_continue = np.multiply(data, np.asarray([1,theta[0],1]))
    ndata = data.copy()
    ndata[:,0] = data[:,1]
    data_continue2 = np.multiply(data, np.asarray([1,theta[1],1]))

    resA = (alpha/len(data)) * np.sum(data_continue, axis=0)
    resB = (alpha/len(data)) * np.sum(data_continue2, axis=0)
    return (theta[0] + resA[1] - resA[2], (theta[1] + resB[1] - resB[2])*resB[0])

'''
h = np.matmul(X, theta)
m, _ = X.shape
return np.matmul((h-y).T,X).T/m
x tiene (m,2)
'''

def costo(data, theta):
    datanueva = data.copy()
    datanueva[:,0] = np.power(theta[0] + (data[:,1] * theta[1]) - data[:,2], 2)
    return 1/(2 * len(data)) * np.sum(datanueva[:,0])

'''
m, _ = X.shape
h = np.matmul(X, theta)
sq = (y - h) ** 2
'''

def gradient_descent(derivative, data, theta, alpha, iteraciones):
    for i in range(iteraciones):
        res = derivative(data, theta, alpha)
        theta[0] -= res[0]
        theta[1] -= res[1]
        print(costo(data, res))
        print(res)
    
# RANDOM DATASET 
# y = 0.6x + 3
x = np.asarray([np.random.randint(250) for i in range(100)]).reshape(100,1)
y = np.asarray([(0.6 * i + (3 * np.random.randint(10))) for i in x]).reshape(100,1)

data = np.hstack((x,y))

# recibo la data 
info = np.hstack((np.ones(100).reshape(100,1), data))
gradient_descent(derivada, info, [100,100], 0.009, 1000)

#plt.scatter(x,y)
#plt.show()



