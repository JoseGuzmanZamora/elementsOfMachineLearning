# José Alejandro Guzmán Zamora 

'''
Reto hacer una funcion para cualquier menu
'''
quemado = {
    "Suma":lambda x: int(x[0]) + int(x[1]),
    "Resta":lambda x: x - y,
    "Multiplicacion":lambda x: x * y
}

def generic_menu(diccionario):
    while(1):
        for valor in diccionario.items():
            print(valor[0])
        respuesta = input("Opción: ")
        print(operacion(respuesta, diccionario[respuesta], 2))


def operacion(nombre, funcion, argumentos):
    print("\n Bienvenido, vamos a realizar la función " + nombre)
    mandar = []
    for i in range(argumentos):
        mandar.append(input("Argumento No. " + str(i + 1) + ": "))
    return funcion(mandar)

generic_menu(quemado)


