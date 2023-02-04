cnt = 0
for i1 in range(8):
    for i2 in range(8):
        for i3 in range(8):
            for i4 in range(8):
                for i5 in range(8):
                    for i6 in range(8):
                        mass = [i1] + [i2] + [i3] + [i4] + [i5] + [i6]
                        if (mass.count(0) + mass.count(1) + mass.count(2) + mass.count(3)) > (mass.count(4) + mass.count(5) + mass.count(6) + mass.count(7)):
                            cnt += 1
print(cnt)