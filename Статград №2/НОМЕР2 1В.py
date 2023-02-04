print('x', 'y', 'z', 'w', 'F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (x == (not y)) or ((not z or not w) and (not w or y)):
                    c = 1
                else:
                    c = 0
                print(x, y, z, w, c)
