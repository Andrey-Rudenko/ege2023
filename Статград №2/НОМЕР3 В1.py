def ABOBA(n, b):
    cnt = 0
    for k in range(len(n)):
        cnt += int(n[k])
    if cnt % 2 != 0:
        b += '1'
    else:
        b += '0'
    return b


for n in range(100, 500):
    b = str(bin(n))[2:]
    b = ABOBA(str(n), b)
    b = ABOBA(str(int(b, 2)), b)
    b = ABOBA(str(int(b, 2)), b)
    print(str(int(b, 2)))





