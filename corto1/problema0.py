
informacion = {
    'unidades':("cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", 
    "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince"), 
    'decenas':("diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", 
    "setenta", "ochenta", "noventa", "cien", "ciento", "cientos")
}

numero = input("Por favor ingrese un entero positivo menor o igual que 1000: ")

if int(numero) < 16:
    print(informacion['unidades'][int(numero)])
elif len(numero) == 2:
    union = informacion['decenas'][int(numero[0]) - 1]
    if numero[1] != '0':
        union += " y " + informacion['unidades'][int(numero[1])]
    print(union)
elif len(numero) == 3:
    union = informacion['unidades'][int(numero[0])] + "cientos "
    if numero[1] != '0':
        union += informacion['decenas'][int(numero[1]) - 1]
    if numero[2] != '0':
        union += " y " + informacion['unidades'][int(numero[2])]
    print(union)
elif int(numero) == 1000:
    print("mil")
else:
    print("Número no válido.")
    
