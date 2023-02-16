for a in range(-1000, 100):
    flg = True
    for x in range(1, 1000):
        if not flg:
            break
        for y in range(1, 1000):
            if not((not(144 % x == 0) or not(x % y == 0)) or (x + y > 100) or (a - x > y)):
                flg = False
                break
    if flg:
        print(a)
