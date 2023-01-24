for i1 in range(111):
    for i2 in range(111):
        for i3 in range(111):
            a = 26
            b = 54
            c = 48
            if (a - i1 - i3 == 0) and \
                    (b - i1 - i2 - i3 * 2 == 0) and (c - i2 - i3 * 2 == 0):
                print(i1 + i2 + i3 + 2)
