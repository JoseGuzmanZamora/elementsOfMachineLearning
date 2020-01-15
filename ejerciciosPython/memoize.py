def memoriza(slow_function):
    anteriores = []
    resultados = []
    if params not in anteriores:
        res = slow_function()
        resultados.append(res)
        anteriores.append(params)
        return res 
    else:
        return resultados[anteriores.index(params)]

def memoized(slow_function):
    return memoriza(slow_function)

