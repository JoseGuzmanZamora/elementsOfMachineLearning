import neural_net
import pandas as pd 

test = pd.read_csv('../../mnist_test.csv')
train = pd.read_csv('../../mnist_train.csv')

print(train.head())
# PARAMETERS SETUP 
# ese 3 es la cantidad de categorias que hay 
'''cat = 3
introduce_y = (new_y == np.arange(cat)).astype(int)
nodes_inicio = [3,3]
thetas = forward_setup(nodes_inicio, xes,introduce_y,2)
ingreso = flatten_zetas(thetas)
print(backward_prop(ingreso[0],ingreso[1],xes,introduce_y))'''