# 19.0
f = open("27989_B.txt")
s = int(f.readline())
n26 = 0
n13 = 0
n2 = 0
for i in range(s):
    a = int(f.readline())
    if a % 26 == 0:
        n26 += 1
    elif a % 13 == 0:
        n13 += 1
    elif a % 2 == 0:
        n2 += 1
print(n26*(n26-1)/2 + n26*(s - n26) + n2 * n13)
