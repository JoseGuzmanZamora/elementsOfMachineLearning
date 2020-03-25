import numpy as np 
import copy 

def sigmoid(values):
    return 1 / (1 + np.exp(-values))

def forward_setup(nodos, X):
    nodos.insert(0,X.shape[1])
    nodos.append(1)
    nodes = [i + 1 for i in nodos]

    # red, mesh de thetas 
    thetas = []
    # por el momento le voy a poner mas 1 por la output layer 
    for i in range(hidden_layers + 1):
        temp_primero = np.expand_dims(np.asarray([1 for i in range(nodes[i])],dtype='float64'),1)
        thetas.append(np.matrix(np.asarray(
            [temp_primero for i in range(nodos[i + 1])]
            )))
    return thetas

def forward_prop(X,thetas):
    inicial = X.T
    trace = [inicial]
    for i in range(len(thetas)):
        interno = np.matmul(
            thetas[i],
            np.vstack(
                [np.expand_dims(np.ones(trace[i].shape[1]),0),
                trace[i]]
                )
        )
        trace.append(sigmoid(interno))
    return trace 

def backward_prop(X,Y,thetas):
    m,_ = X.shape
    delta = copy.deepcopy(thetas)
    for i in delta: i[:] = 0
    activation_trace = forward_prop(X,thetas)
    first_delta = activation_trace[-1] - Y.T
    deltas = [first_delta]
    # backward prop 
    for i in reversed(range(1,len(thetas))):
        first_delta = np.multiply(
            np.matmul(thetas[i].T[1:,:],first_delta),
            np.multiply(activation_trace[i],(1-activation_trace[i]))
            )
        deltas.append(first_delta)

    deltas = list(reversed(deltas))
    for i in range(len(delta)):
        print("Aim: ",delta[i].T.shape)
        print(activation_trace[i + 1].shape)
        print(deltas[i].T.shape)


# DATASET FICTICIO
valores = 10
def random_variable(n):
    x = np.asarray([np.random.randint(0,100) for i in range(n)])
    return np.expand_dims(x,1)

x_1 = random_variable(valores)
x_2 = random_variable(valores)
'''ones = np.expand_dims(
    np.asarray([1 for i in range(valores)]),
    1
)'''

# aqui ya tenemos el formato esperado de las equises, como columnas  
xes = np.hstack([x_1,x_2])

# aqui ya tenemos el formato esperado de las yes, como columnas tmb
y = [0 if x_1[i] > 50 else 1 for i in range(valores)]
y = np.expand_dims(np.asarray(y), 1)

# PARAMETERS SETUP 
hidden_layers = 8
nodes_inicio = [3,3,3,6,5,2,8,9]

# LLAMADA A LA FUNCION
thetas = forward_setup(nodes_inicio, xes)
activations = forward_prop(xes,thetas)
backward_prop(xes,y, thetas)
