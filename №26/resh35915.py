f = open('26 .35915.txt')
s = int(f.readline())
mass = []
mass1 = []
for i in range(s):
    a = int(f.readline())
    mass.append(a)
    if a % 2 != 0:
        mass1.append(a)
print(len(mass1))
cnt = 0
mmx = 0
for i in range(len(mass1) - 1):
    for j in range(i+1, len(mass1) - 1):
        if (mass1[i] + mass1[j]) % 2 == 0:
            if (mass1[i] + mass1[j])/2 in mass:
                cnt += 1
                mmx = max(mmx, (mass1[i] + mass1[j])/2)
print(cnt, mmx)

