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

# aqui ya tenemos el formato esperado de las yes, como columnas tmb
y = [0 if x_1[i] > 50 else 1 for i in range(5)]
y = np.expand_dims(np.asarray(y), 1)

# PARAMETERS SETUP 
hidden_layers = 2 
nodes_inicio = [4,3]
nodes = [3,5,4,1]

cantidad_thetas_layers = hidden_layers + 1

# red, mesh de thetas 
thetas = []
# por el momento le voy a poner mas 1 por la output layer 
for i in range(hidden_layers + 1):
    temp_primero = np.asarray([0 for i in range(nodes[i])])
    temp_primero = np.expand_dims(temp_primero,1)
    temp_segundo = np.asarray([temp_primero for i in range(nodes[i + 1])])
    thetas.append(temp_segundo)


prueba = np.asarray(thetas)
print(prueba)
print(prueba[0][0])



