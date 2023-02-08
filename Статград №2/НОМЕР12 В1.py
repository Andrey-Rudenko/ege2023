import itertools
a = 0
max3 = []
for x in itertools.product('12', repeat=20):
    s = ''.join(x)
    if s.count('1') == 10 and s.count('2') == 10:
        s = '0' + s + '0'
        while '00' not in s:
            s = s.replace('012', '30', 1)
            if '011' in s:
                s = s.replace('011', '20', 1)
                s = s.replace('022', '40', 1)
            else:
                s = s.replace('01', '10', 1)
                s = s.replace('02', '101', 1)
        if s.count('1') == 7 and s.count('2') == 5:
            max3.append(s.count('3'))
print(max(max3))



