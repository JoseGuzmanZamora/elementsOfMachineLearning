import numpy as np 
import matplotlib.pyplot as plt 

def cost(X,Y,thetas):
    """ 
    Calcular el costo de un conjunto de hipótesis basado en 
    la cantidad de thetas ingresados.
    """
    hipos = np.matmul(X, thetas)
    return np.sum(np.power(hipos - Y, 2)) / (2 * X.shape[0])

def derivative(X,Y,thetas):
    """
    Encontrar la derivada de la función de costo y retornar 
    la suma de todas las hipótesis.
    """
    hips = np.matmul(X, thetas)
    interno = (hips - Y).transpose()
    return (np.matmul(interno, X) / X.shape[0]).transpose()

def gradient_descent(X, Y, thetas, a, it, delta):
    """
    Aplica descenso del gradiente en base a un dataset y thetas iniciales.

    Params:
    - X : valores de x con columna de 1s agregada al inicio
    - Y : valores de entrenamiento
    - a : learning rate
    - it : cantidad de iteraciones
    - delta : cambio mínimo para parar las iteraciones
    """
    costos = []
    procesado = np.asarray(thetas, dtype='float64').reshape(len(thetas),1)
    for i in range(it):
        costo1 = np.round(cost(X,Y,procesado),4)
        procesado -= a * derivative(X,Y,procesado)
        costo = np.round(cost(X,Y,procesado),4)
        costos.append("H(" + str(i) + ") =" + str(procesado) + " costo -> " + str(costo))
        if np.absolute(costo1 - costo) <= delta:
            print(i)
            break
    return (procesado,costos)


'''# RANDOM DATASET 
# y = 0.6x + 3
x = np.asarray([np.random.randint(250) for i in range(100)]).reshape(100,1)
ys = np.asarray([(0.6 * i + (3 * np.random.randint(10))) for i in x]).reshape(100,1)

# recibo la data 
xs = np.hstack((np.ones(100).reshape(100,1), x))

thetas = [9,4]
res = gradient_descent(xs, ys, thetas, 0.00001, 1000, 0.0005)
print(res)

plt.scatter(x,ys)
x = np.linspace(0,250,100)
y = res[1] * x + res[0]
plt.plot(x, y, '-r')
plt.show()'''





