def funct(var):
    p = 0
    af = []
    for i in range(0, var):
        if(i%2 != 0):
            p += i*i
            af.append(i*i)
    print(sum(af))
    print(p)
funct(36)
