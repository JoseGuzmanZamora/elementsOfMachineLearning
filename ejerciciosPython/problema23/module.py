# José Alejandro Guzmán Zamora 

'''
Instrucciones 
Escriba un programa que lea los contenidos de triangle.txt
, y calcule el camino de adyacentes que suma el total más largo.
'''

archivo = open("triangle.txt","r")

primer_separacion = archivo.read().split('\n')

for i in range(len(primer_separacion)):
    primer_separacion[i] = primer_separacion[i].split(' ')

general = int(primer_separacion[0][0])

def vecinos(ubicacion):
    y = ubicacion[0]
    x = ubicacion[1]
    vecindario = []
    ubicaciones = []
    vecindario.append(primer_separacion[y + 1][x])
    ubicaciones.append(((y + 1),x))
    vecindario.append(primer_separacion[y + 1][x + 1])
    ubicaciones.append(((y + 1), (x + 1)))
    return ubicaciones[vecindario.index(max(vecindario))]



siguiente = vecinos((0,0))
for i in range(1,len(primer_separacion)):
    general += int(primer_separacion[siguiente[0]][siguiente[1]])
    if i < len(primer_separacion) - 1:
        siguiente = vecinos(siguiente)
print(general)


