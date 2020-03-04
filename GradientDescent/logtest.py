import numpy as np 
import matplotlib.pyplot as plt 
import logistic 


# Crear primer dataset ficticio 

x1 = [np.random.uniform(0,1) for i in range(200)]
x2 = [np.random.uniform(0,1) for i in range(200)]
antes = [1 for i in range(len(x1))]
data = np.vstack([antes,x1,x2]).transpose()


y = []
for i in range(len(x1)):
    if x1[i] > 0.5:
        if x2[i] > 0.5:
            y.append(1)
        else:
            y.append(0)
    else:
        y.append(0)

ys = np.asarray(y).reshape(len(y), 1)
thetas = [0,0,0]
thetas = np.asarray(thetas, dtype='float64').reshape(len(thetas), 1)

print(data)
resultado = logistic.gradient_descent(data, ys, thetas, 0.0013, 100000)
thetas = resultado[len(resultado) - 1][0]
intercept = - thetas[0] / thetas[1]
slope = - thetas[2] / thetas[1] 

xp = np.linspace(0,1,100)
yp = slope * xp + intercept

plt.scatter(x1, x2, c=y, cmap=plt.cm.Paired)
plt.plot(xp, yp, '-r')
plt.show()

it = [i for i in range(len(resultado))]

costos = [i[1] for i in resultado]
plt.plot(it, costos)
plt.show()


# circulo
y2 = []
for i in range(len(x1)):
    if x1[i] > 25 and x1[i] < 75:
        if x2[i] > 25 and x2[i] < 75:
            y2.append(1)
        else:
            y2.append(0)
    else:
        y2.append(0)
ys2 = np.asarray(y2).reshape(len(y2), 1)

# features polinomicas 
x1_squared = [i ** 2 for i in x1]
x2_squared = [i ** 2 for i in x2]
data2 = np.vstack([antes,x1,x1_squared,x2,x2_squared]).transpose()
plt.scatter(x1, x2, c=y2, cmap=plt.cm.Paired)
plt.show()
