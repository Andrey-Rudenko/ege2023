a = 9 ** 8 + 3 ** 5 - 9
c = ''
while a > 0:
    c += str(a % 3)
    a = a // 3
print(c)