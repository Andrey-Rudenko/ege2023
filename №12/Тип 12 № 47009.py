for i1 in range(19):
    for i2 in range(19):
        for i3 in range(19):
            a = 61
            b = 50
            c = 18
            if (a - i3 * 3 - i2 * 2 - i1 == 0) and (b - i3 * 3 - i2 - i1 == 0) and (c - i3 - i2 == 0):
                print(i1 + i2 + i3 + 2)

