f = open('26.47230.txt')
s = int(f.readline())
mass = []
for i in range(s):
    a = int(f.readline())
    mass.append(a)
mass.sort(reverse=True)
cnt = 1
min_max = 0
max1 = mass[0]
for i in range(len(mass) - 2):
    if max1 - mass[i] >= 3:
        cnt += 1
        max1 = mass[i]
        min_max = mass[i]
print(cnt, min_max)
print(mass)
