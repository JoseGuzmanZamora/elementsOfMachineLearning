# José Alejandro Guzmán Zamora 

'''
Reto hacer una funcion para cualquier menu
'''

quemado = {
    "opcion1":"Resultado1",
    "opcion2":"Resultado2",
    "opcion3":"Resultado3"
}

def generic(diccionario):
    x = lambda opcion : print(opcion)
    y = lambda resultado : print(resultado)
    for valor in diccionario.items():
        x(valor[0])
    opcion = input("Opcion")
    


generic(quemado)