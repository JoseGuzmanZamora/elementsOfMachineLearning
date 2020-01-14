

def generic_menu(diccionario):
    """
    Builds a generic menu from the configuration dictionary. 

    Arguments:
        diccionario -- dictionary where the keys are the options for the 
        menu and the value is the function to execute after getting chosen 
        nargumentos
    Returns:
        Results from function operacion, generic function evaluator
    """ 
    while(1):
        for valor in diccionario.items():
            print(valor[0])
        respuesta = input("Opción: ")
        if respuesta in diccionario:
            pasar = diccionario[respuesta]
            print(operacion(respuesta, pasar[0], pasar[1]))
        elif respuesta == " ":
            break
        else:
            print("Opción no válida.")


def operacion(nombre, funcion, argumentos):
    """
    Starts and evaluates the function passed as parameter. 

    Arguments:
        nombre -- String that represents the name of the function
        funcion -- lambda function to evaluate
        argumentos -- number of parameters to pass 
    Returns:
        Call to function with the specific parameter
    """
    print("\n Bienvenido, vamos a realizar la función " + nombre)
    mandar = []
    for i in range(argumentos):
        mandar.append(input("Argumento No. " + str(i + 1) + ": "))
    return funcion(mandar)


"""
Example call. 

The dictionary has keys that represent the menu. The value of each key 
is a lambda function that can be changed. Note that the lambda is
inside a list, it is paired with the amount of parameters needed to 
run the function. 
"""
quemado = {
    "Suma": [lambda x: int(x[0]) + int(x[1]), 2],
    "Resta": [lambda x: int(x[0]) - int(x[1]), 2],
    "Multiplicacion": [lambda x: int(x[0]) * int(x[1]), 2],
}

#main call 
generic_menu(quemado)


