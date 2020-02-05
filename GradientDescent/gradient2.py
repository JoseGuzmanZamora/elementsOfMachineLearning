# Gradient Descent Vectorial

import numpy as np 
import matplotlib.pyplot as plt

def derivada(data, theta, alpha):
    data_continue = np.multiply(data, np.asarray([1,theta[0],1]))
    ndata = data.copy()
    ndata[:,0] = data[:,1]
    data_continue2 = np.multiply(data, np.asarray([1,theta[1],1]))

    resA = np.sum(data_continue * (alpha/len(data)), axis=0)
    resB = np.sum(data_continue2 * (alpha/len(data)), axis=0)
    return (theta[0] + resA[1] - resA[2], (theta[1] + resB[1] - resB[2])*resB[0])

def gradient_descent(derivative, data, theta, alpha):
    while 1:
        res = derivative(data, theta, alpha)
        if abs(theta[0] - res[0]) <= 0.0001:
            print(res)
            break
        theta[0] -= res[0]
        theta[1] -= res[1]
    
# RANDOM DATASET 
# y = 0.6x + 3
x = np.asarray([np.random.randint(250) for i in range(100)]).reshape(100,1)
y = np.asarray([(0.6 * i + (3 * np.random.randint(10))) for i in x]).reshape(100,1)

data = np.hstack((x,y))

# recibo la data 
info = np.hstack((np.ones(100).reshape(100,1), data))
gradient_descent(derivada, info, [0,0], 0.01)

plt.scatter(x,y)
plt.show()



