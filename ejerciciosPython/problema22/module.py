# José Alejandro Guzmán Zamora 
import numpy as np 

def distancia(punto1,punto2):
    return np.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

def verificacion(tuplas):
    #ver las distancias 
    distancia1 = distancia(tuplas[0], tuplas[1])
    distancia2 = distancia(tuplas[0], tuplas[2])
    distancia3 = distancia(tuplas[0], tuplas[3])
    distancias = [distancia1, distancia2, distancia3]
    
    primer_diagonal = distancias.index(max(distancias))

    del tuplas[primer_diagonal + 1]
    distancia_siguiente = distancia(tuplas[1], tuplas[2])
    
    if max(distancias) == distancia_siguiente:
        print("Sí es cuadrado.")
    else:
        print("No es cuadrado.")


paralelogramo = [(4,0),(0,0),(4,4),(0,4)]
verificacion(paralelogramo)



