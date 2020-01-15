numero = 7 

def factorial(n):
    tmp = n
    for i in range(n - 1,1,-1):
        tmp *= i
    return tmp 


better_factorial = lambda n: reduce(lambda a,b: a * b, range(1,n + 1))
print(factorial(6))