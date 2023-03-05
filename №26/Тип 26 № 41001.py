f = open('26.txt')
all_proc = int(f.readline())
proc_start = []
proc_end = []
for i in range(all_proc):
    a = f.readline().split()
    proc_start.append(int(a[0]))
    proc_end.append(int(a[1]))
proc_end.sort()
proc_start.sort()

cnt = 0
t = 1
max_proc = 0

while proc_start[0] == 0:
    cnt += 1
    proc_start.pop(0)
while proc_end[0] == 0:
    proc_end.pop(0)

t = min(proc_end[0], proc_start[0])

while t <= 1633305600 + 604800:
    while proc_start[0] == t:
        cnt += 1
        proc_start.pop(0)
    while proc_end[0] == t:
        cnt -= 1
        proc_end.pop(0)
    if 1633305600 <= t <= 1633305600 + 604800:
        if max_proc < cnt:
            max_proc = cnt
    t = min(proc_end[0], proc_start[0])

print(max_proc)



