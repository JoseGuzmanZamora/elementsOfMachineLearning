# José Alejandro Guzmán Zamora 
import numpy as np 

'''
Instrucciones 
Dadas cuatro tuplas (en ningún orden en particular) representando 
cuatro puntos en un espacio bidimensional, determine si en conjunto 
representan un cuadrado.
'''

tuplas = [(0,5),(-5,0),(5,0),(0,-5)]


distancia1 = np.sqrt((tuplas[0][0] - tuplas[1][0])**2 + (tuplas[0][1] - tuplas[1][1])**2)
distancia2 = np.sqrt((tuplas[0][0] - tuplas[2][0])**2 + (tuplas[0][1] - tuplas[2][1])**2)
distancia3 = np.sqrt((tuplas[0][0] - tuplas[3][0])**2 + (tuplas[0][1] - tuplas[3][1])**2)

distancias = [distancia1, distancia2, distancia3]
primer_diagonal = distancias.index(max(distancias))

del tuplas[primer_diagonal + 1]

distancia_siguiente = np.sqrt((tuplas[1][0] - tuplas[2][0])**2 + (tuplas[1][1] - tuplas[2][1])**2)

print(primer_diagonal)

if max(distancias) == distancia_siguiente:
    print("Si es cuadrado")
else:
    print("No es cuadrado")



