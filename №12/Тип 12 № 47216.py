for n in range(0, 100):
    # b = ">" + "0" * 39 + '1' * n + "2" * 39
    # while (">1" in b) or (">2" in b) or (">0" in b):
    #     if ">1" in b:
    #         b = b.replace(">1", "22>", 1)
    #     if ">2" in b:
    #         b = b.replace(">2", "2>", 1)
    #     if ">0" in b:
    #         b = b.replace(">0", "1>", 1)
    b = 117 + n * 4
    flg = True
    for i in range(2, b):
        if b % i == 0:
            flg = False
            break
    if flg:
        print(b, n)



