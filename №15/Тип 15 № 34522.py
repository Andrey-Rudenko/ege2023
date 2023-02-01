for a in range(1500):
    flg = True
    for x in range(1000):
        if not((x & 51 == 0) or (not (x & 41 == 0) or (x & a == 0))):
            flg = False
    if flg:
        print(a)
