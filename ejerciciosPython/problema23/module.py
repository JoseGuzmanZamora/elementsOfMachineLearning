# José Alejandro Guzmán Zamora 

'''
Instrucciones 
Escriba un programa que lea los contenidos de triangle.txt
, y calcule el camino de adyacentes que suma el total más largo.
'''

archivo = open("triangle.txt","r")

info = archivo.read().split('\n')

for i in range(len(info)):
    info[i] = info[i].split(' ')

# Ya tenemos la informacion ahora hay que recorrer de abajo hacia arriba 

for i in range(len(info) - 1, -1, -1):
    '''for j in range(len(info[i]) - 1):
        mayor = max(info[i][j], info[i][j + 1])
        info[i - 1][j] += mayor'''
    for j in range(len(info[i]) - 1):
        mayor = max(info[i][j], info[i][j + 1])
        info[i - 1][j] = int(info[i - 1][j]) + int(mayor)
    print(info[i])
