# First Version of Gradient Descent specifically made for Linear Regression 

def actualizacion(train,theta0,theta1,alpha,step):
    m = len(train)
    if step:
        lista = [theta0 + (theta1 * train[i][0]) 
                - train[i][1] for i in range(m)]
    else:
        lista = [(theta0 + (theta1 * train[i][0]) 
                - train[i][1]) * train[i][0] for i in range(m)]
    return (alpha / m) * sum(lista)

def gradient_descent(train, alpha):
    zeta = [1,0]
    while 1:
        temp0 = zeta[0] - actualizacion(train, zeta[0], zeta[1], alpha, True)
        temp1 = zeta[1] - actualizacion(train, zeta[0], zeta[1], alpha, False)
        zeta[0] = temp0
        zeta[1] = temp1
    return zeta


dataset = [[2,5],[3,6],[4,9],[5,9],[9,12]]
alpha = 1.5
print(gradient_descent(dataset, alpha))