f = open('26(2).txt')
al = int(f.readline())
values = []
for i in f:
    values.append(int(i))
values.sort(reverse=True)
print(values)
cnt = 1
a = values[0]
for i in range(1, len(values)):
    if a - values[i] >= 3:
        cnt += 1
        a = values[i]
print(cnt, a)
