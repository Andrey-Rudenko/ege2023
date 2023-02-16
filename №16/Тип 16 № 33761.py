def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n/2)
    elif n % 2 != 0:
        return 1 + f(n-1)

for i in range(0, 10000):
    if f(i) == 11:
        print(i)
