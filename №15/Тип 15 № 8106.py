for a in range(1, 1000):
    flg = True
    for x in range(1, 1000):
        if not((x % a == 0) or(not(x % 6 == 0) or not(x % 4 == 0))):
            flg = False
            break
    if flg:
        print(a)