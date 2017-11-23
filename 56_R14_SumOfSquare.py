def funct(integer):
    sqr = []
    p = 0
    for i in range(0, integer):
        sqr.append(i*i)
        p += i*i
    print(sqr)
    print(p)
    y = sum(sqr)
    print(y)

funct(36)


