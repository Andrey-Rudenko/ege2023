f = open('26 .35915.txt')
all_nums = int(f.readline())
nums = [int(i) for i in f]
nums_ne = []

nums.sort()
nums_ne.sort()

for i in nums:
    if i % 2 != 0:
        nums_ne.append(i)
print(len(nums_ne))
cnt = 0
for i in range(len(nums_ne) - 1):
    for j in range(i+1, len(nums_ne)):
        if (nums_ne[i] + nums_ne[j] // 2) in nums:
            cnt += 1
print(cnt)


