def es_palindromo(n):
    numero = str(n)
    if len(numero) % 2 == 0:
        normal = [i for i in numero]
        invertido = normal.copy()
        invertido[::-1] = normal[::]
        if invertido == normal:
            return True 
        else: 
            return False 
    else:
        return False

def invertir(n):
    numero = str(n)
    normal = [i for i in numero]
    invertido = normal.copy()
    invertido[::-1] = normal[::]
    retornar = ''
    for i in invertido:
        retornar += i 
    return retornar

def verificacion(n):
    primera = es_palindromo(n)
    if not primera:
        continuar = True
        numero = n 
        contador = 0
        while continuar:
            invertido = invertir(numero)
            siguiente = n + int(invertido)
            continuar = es_palindromo(siguiente)
            numero = siguiente
            if contador > 50:
                return False 
        return True 

#verificacion 
general = 0
for i in range(1001):
    resultado = verificacion(i)
    if not resultado:
        general += 1

print("Cantidad de Lychrel Numbers: ", general)


