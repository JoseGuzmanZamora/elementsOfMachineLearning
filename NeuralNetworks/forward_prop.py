import numpy as np 

def sigmoid(values):
    return 1 / (1 + np.exp(-values))

def forward_setup(nodos, X):
    nodos.insert(0,X.shape[1] - 1)
    nodos.append(1)
    nodes = [i + 1 for i in nodos]

    # red, mesh de thetas 
    thetas = []
    # por el momento le voy a poner mas 1 por la output layer 
    for i in range(hidden_layers + 1):
        temp_primero = np.asarray([1 for i in range(nodes[i])])
        temp_primero = np.expand_dims(temp_primero,1)
        temp_segundo = np.asarray([temp_primero for i in range(nodos[i + 1])])
        thetas.append(np.matrix(temp_segundo))
    return thetas

def forward_prop(X,thetas):
    inicial = X.T
    for i in range(hidden_layers + 1):
        respuesta_interna = sigmoid(np.matmul(thetas[i], inicial))
        bias = [1 for i in range(respuesta_interna.shape[1])]
        inicial = np.vstack([bias, respuesta_interna])
    return inicial[1].T




# DATASET FICTICIO
valores = 100
def random_variable(n):
    x = np.asarray([np.random.randint(0,100) for i in range(n)])
    return np.expand_dims(x,1)

x_1 = random_variable(valores)
x_2 = random_variable(valores)
ones = np.expand_dims(
    np.asarray([1 for i in range(valores)]),
    1
)

# aqui ya tenemos el formato esperado de las equises, como columnas  
xes = np.hstack([ones,x_1,x_2])

# aqui ya tenemos el formato esperado de las yes, como columnas tmb
y = [0 if x_1[i] > 50 else 1 for i in range(valores)]
y = np.expand_dims(np.asarray(y), 1)

# PARAMETERS SETUP 
hidden_layers = 2 
nodes_inicio = [5,3,3]

# LLAMADA A LA FUNCION
thetas = forward_setup(nodes_inicio, xes)
res = forward_prop(xes,thetas)
print(res)
