import numpy as np 
import copy 

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
        temp_primero = np.expand_dims(np.asarray([1 for i in range(nodes[i])]),1)
        thetas.append(np.matrix(np.asarray(
            [temp_primero for i in range(nodos[i + 1])]
            )))
    return thetas

def forward_prop(X,thetas):
    inicial = X.T
    trace = []
    for i in thetas:
        respuesta_interna = sigmoid(np.matmul(i, inicial))
        inicial = np.vstack(
            [np.ones(respuesta_interna.shape[1]), respuesta_interna]
            )
        trace.append(inicial)
    return trace 

def backward_setup(X,Y,thetas):
    m,_ = X.shape
    delta = copy.deepcopy(thetas)
    # set delta = 0 for all i,j,l 
    for i in delta: i[:] = 0
    activation_trace = forward_prop(X,thetas)
    first_res = activation_trace[-1][1].T
    first_delta = first_res - Y 
    backward_prop(activation_trace[:-1],thetas, first_delta)
    
def backward_prop(trace,thetas, delta_one):
    deltas = []
    siguiente_delta = delta_one
    print(thetas)
    for i in reversed(range(0,len(trace))):
        if (i + 1) == len(thetas) - 1:
            siguiente_delta = np.matmul(thetas[i+1].T,siguiente_delta)
        else:
            print(thetas[i + 1][1:].shape)
            print(siguiente_delta.shape)
            siguiente_delta = np.matmul(thetas[i + 1][1:].T,siguiente_delta)


# DATASET FICTICIO
valores = 1
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
nodes_inicio = [3,4]

# LLAMADA A LA FUNCION
thetas = forward_setup(nodes_inicio, xes)
backward_setup(xes,y, thetas)
