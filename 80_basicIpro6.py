def inserting(var):
    l = [0]*var
    for i in range(var):
        l[i]= int(input("Enter Value: "))
    print(l)
    print(tuple(l))
inserting(5)
