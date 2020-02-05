# Gradient Descent Vectorial

import numpy as np 

def derivada(data, theta, alpha):
    vector1 = np.asarray([1,theta[0],1])
    vector2 = np.asarray([1,theta[1],1])
    print(vector1)
    data_continue = np.multiply(data, vector1)
    print(data_continue)


# RANDOM DATASET 

x = np.asarray([np.random.randint(250) for i in range(100)]).reshape(100,1)
y = np.asarray([np.random.randint(250) for i in range(100)]).reshape(100,1)

data = np.hstack((x,y))

# recibo la data 
info = np.hstack((np.ones(100).reshape(100,1), data))

derivada(info, (3,7),5)



