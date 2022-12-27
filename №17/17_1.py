f = open('17_1.txt')
mass = []
for i in f:
    mass.append(int(i))
minn = min(mass)
cnt = 0
mx = 0
for i in range(len(mass) - 1):
    if mass[i] % 111 == minn or mass[i + 1] % 111 == minn:
        cnt += 1
        mx = max(mx, mass[i] + mass[i + 1])
print(cnt, mx)