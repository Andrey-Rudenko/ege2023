cnt = 0
for a in range(500):
    flg = True
    for x in range(1000):
        if not flg:
            break
        for y in range(1000):
            if not((not(x < 6) or (x**2 < a)) and (not(y ** 2 <= a) or (y <= 6))):
                flg = False
                break
    if flg:
        cnt += 1
print(cnt)