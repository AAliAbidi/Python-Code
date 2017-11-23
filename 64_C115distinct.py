def distinct(value):
    l = [0]*value
    for i in range(value):
        l[i] = int(input("Enter value: "))
    print(l)
    variable = l[0]
    distinctArray = []
    for k in range(0, value-1):
        if(l[k+1]==variable):
            distinctArray.append(variable)
            variable = l[k]
    print(distinctArray)
distinct(5)
