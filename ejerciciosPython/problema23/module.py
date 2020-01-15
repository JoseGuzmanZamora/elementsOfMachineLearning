"""
Largest Sum Module.

Functions:
    abrir_archivo -- opens file from directory 
    recorrido -- finds the largest sum path in a triangle
"""

def abrir_archivo(name):
    """Open file from name and separate by whitespace."""
    with open(name) as file:
        data = file.read().split('\n')
    return [i.split(' ') for i in data]

def recorrido(info):
    """
    Bottom up path through the triangle. 
    
    It starts finding the largest number from each pair in each row 
    and then adds it to its corresponding father until reaching the 
    top.
    
    Arguments:
        info -- Matrix that represents the triangle.
    Returns:
        Largest sum from path
    """
    for i in range(len(info) - 1, -1, -1):
        for j in range(len(info[i]) - 1):
            mayor = max(info[i][j], info[i][j + 1])
            info[i - 1][j] = int(info[i - 1][j]) + int(mayor)
    return info[0]


