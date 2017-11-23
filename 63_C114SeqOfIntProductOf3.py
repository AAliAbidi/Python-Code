def short(value):
    l = [0]*value
    for i in range(value):
        l[i] = int(input("Enter Value: "))
    print("Integer Array is: \n", l)
    firstint = l[0]
    newArray = []
    for k in range(0, value-1):
        if(((l[k+1]*firstint)%2) !=0):
            newArray.append(firstint)
            newArray.append(l[k+1])
            firstint = l[k+1]
    print(newArray)
short(5)
    


