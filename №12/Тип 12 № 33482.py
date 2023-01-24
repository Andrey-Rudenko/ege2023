for i in range(101, 500):
    b = "1" *i
    while "111" in b:
        b = b.replace("111", "22", 1)
        b = b.replace("222", "11", 1)

    print(i, len(b), b, b.count("1"))
