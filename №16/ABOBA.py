import math

def f(n,m):
    a = math.factorial(n)
    b = math.factorial(m)
    return b/(math.factorial(m - n) * a)


print(f(3,30))



