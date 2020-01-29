# José Alejandro Guzmán Zamora


def actualizacion(train,theta0,theta1,alpha,step):
    """
    Aplicación de derivadas parciales a theta 1 y theta 2. 

    Params:
        - train : dataset de entrenamiento 
        - theta0 : valor actual de theta 0 
        - theta1 : valor actual de theta 1 
        - alpha : learning rate 
        - step : True para modificar theta0, False para theta1
    Returns:
        - Resultado de operación
    """
    m = len(train)
    if step:
        lista = [theta0 + (theta1 * train[i][0]) 
                - train[i][1] for i in range(m)]
    else:
        lista = [(theta0 + (theta1 * train[i][0]) 
                - train[i][1]) * train[i][0] for i in range(m)]
    return (alpha / m) * sum(lista)

def gradient_descent(train, alpha, iteraciones):
    """
    Aplica Gradient Descent sobre un dataset de entrenamiento. 

    Params:
        - train : valores x y y para entrenamiento 
        - alpha : training rate 
        - iteraciones : indica cuántas iteraciones realizar 
    Returns:
        - Theta 0 y theta 1 finales 
    """
    zeta = [0,0]
    for i in range(iteraciones):
        temp0 = zeta[0] - actualizacion(train, zeta[0], zeta[1], alpha, True)
        temp1 = zeta[1] - actualizacion(train, zeta[0], zeta[1], alpha, False)
        zeta[0] = temp0
        zeta[1] = temp1
    return zeta

# Prueba 
dataset = [[2,5],[3,6],[4,9],[5,9],[9,12]]
alpha = 0.5
print(gradient_descent(dataset, alpha, 100))