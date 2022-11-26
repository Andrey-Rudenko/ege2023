f = open('27887.txt')
s = f.readline().split()
max_mem = int(s[0])
s2 = int(s[1])
mass = []
for i in range(s2):
    mass.append(int(f.readline()))
mass.sort()
print(mass)
mem = 0
mex = 0
cnt = 0
while (mem + mass[0]) <= max_mem:
    mem += mass[0]
    mex = mass[0]
    mass.pop(0)
    cnt += 1
print(cnt, max_mem - mem + mex)
