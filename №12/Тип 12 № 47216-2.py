def f(b):
    flg =True
    for i in range(2, b):
        if b % i == 0:
            flg = False
    if flg:
        return 'yes'
    else:
        return 'no'

for n in range(101):
    c = 117 + n*4
    if f(c) == 'yes':
        print(n)

