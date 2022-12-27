f = open('17dosrok.txt')
mass = []
for i in f:
    mass.append(int(i))
min23 = 100001
for i in range(len(mass)):
    if mass[i] % 23 == 0:
        min23 = min(min23, mass[i])
mxs = -100001
cnt = 0
for i in range(len(mass) -1):
    if mass[i] % min23 == 0 or mass[i + 1] % min23 == 0:
        cnt += 1
        mxs = max(mxs, mass[i] + mass[i + 1])
print(cnt, mxs)
