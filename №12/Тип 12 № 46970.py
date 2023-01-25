for i1 in range(80):
    for i2 in range(80):
        for i3 in range(80):
            n1 = i1 + i2 * 2 + i3 * 3
            n2 = i1 + i2     + i3 * 3
            n3 =      i2     + i3
            if n1 == 70 and n2 == 56 and n3 == 23:
                print(i1+i2+i3+2)
