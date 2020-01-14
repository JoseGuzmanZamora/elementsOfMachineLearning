"""
Square Verification Module. 

Functions:
    distancia -- finds the distance between two points 
    verificacion -- checks if 4 points represent a square
"""

import numpy as np 

def distancia(punto1,punto2):
    """Applies the distance formula between two points."""
    return np.sqrt(((punto1[0]-punto2[0]) ** 2) 
                    + ((punto1[1]-punto2[1]) ** 2))

def verificacion(tuplas):
    """Evaluates the two diagonals in a quadrilateral.
    
    Arguments:
        Tuplas -- List with 4 tuples representing the quadrilateral
    Returns:
        Boolean True in case it representes a square and vice versa
    """

    distancias = [distancia(tuplas[0], tuplas[i]) for i in range(1,len(tuplas))]
    
    primer_diagonal = max(distancias)
    ubicacion_diagonal = distancias.index(primer_diagonal)
    del tuplas[ubicacion_diagonal + 1]

    segunda_diagonal = distancia(tuplas[1], tuplas[2])
    
    if primer_diagonal == segunda_diagonal:
        return True
    return False 