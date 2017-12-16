def fun():
    ary=[]
    j = 0
    for i in range(0, 10):
        j = i
        i = i+1
        ary.append(j*i)
    print (ary)
fun()
