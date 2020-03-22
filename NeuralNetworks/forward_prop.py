import numpy as np 


# Dataset ficticio 
def random_variable(n):
    x = np.asarray([np.random.randint(0,100) for i in range(n)])
    return np.expand_dims(x,1)

x_1 = random_variable(5)
x_2 = random_variable(5)
ones = np.expand_dims(
    np.asarray([1 for i in range(5)]),
    1
)

# aqui ya tenemos el formato esperado de las equises, como columnas  
xes = np.hstack([ones,x_1,x_2])

y = [0 if x_1[i] > 50 else 1 for i in range(5)]

hidden_layers = 1
units_layers = [8]


