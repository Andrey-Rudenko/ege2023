f = (open('27990_b.txt'))
cnt = int(f.readline())
cnt62 = 0
cnt2 = 0
cnt31 = 0

for i in range(cnt):
    a = int(f.readline())
    if a % 62 == 0:
        cnt62 += 1
    elif a % 2 == 0:
        cnt2 += 1
    elif a % 31 == 0:
        cnt31 += 1

sum62 = int((cnt62*(cnt62 - 1))/2)
sum62_n = cnt62*(cnt - cnt62)
sum312 = cnt2 * cnt31
print(sum62+sum312+sum62_n)

