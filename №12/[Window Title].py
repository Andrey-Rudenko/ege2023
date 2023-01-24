a = '8' * 68
print(a)
while ("888" in a) or ("222" in a):
    if "222" in a:
        a = a.replace("222", "8", 1)
    else:
        a = a.replace("888", "2", 1)
print(a)








