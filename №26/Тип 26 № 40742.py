# f = open("26.txt")
# n = int(f.readline())
# start_time = 1633305600
# end_time = start_time + 604800
# count = 0
# time_process = [0 for i in range(0, 604801)]
# for i in f:
#     start_process, end_process = i.split()
#     if (int(start_process) < start_time) and ((int(end_process) > start_time) or (int(end_process) == 0)):
#         count = count + 1
#     if (int(start_process) >= start_time) and (int(start_process) <= end_time):
#         time_process[int(start_process) - start_time] = time_process[int(start_process) - start_time] + 1
#     if (int(end_process) >= start_time) and (int(end_process) <= end_time):
#         time_process[int(end_process) - start_time] = time_process[int(end_process) - start_time] - 1
# print(time_process)
# print(count)
# sum_time = 0
# print(min(time_process))
# max_process = 0
# for i in range(1, 604801):
#     count = count + time_process[i]
#     if count > max_process:
#         max_process = count
#         sum_time = 0
#     if count == max_process:
#         sum_time = sum_time + 1
# print(max_process, sum_time)





import time

start = time.time() ## точка отсчета времени

##код программы





f = open('26.txt')
cntall = int(f.readline())
massiv = []
for i in f:
    a = i.split(' ')
    a[1]= a[1][:-1]
    a = list(map(int, a))
    massiv.append(a)
mass = []
lcnt = 0
for i in range(len(massiv)):
    if massiv[i] == [0, 0]:
        lcnt += 1
    elif massiv[i][0] <= 1633910400 and (massiv[i][1] > 1633305600 or massiv[i][1] == 0):
        mass.append(massiv[i])
print(lcnt)
print(len(mass))
maxcnt = 0
print(mass)

for i in range(1633305600, 1633305600 + 2000):
    cnt = 0
    for j in mass:
        if j[0] <= i or j[1] > i:
            cnt += 1
    maxcnt = max(cnt, maxcnt)
print(maxcnt)



end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени


