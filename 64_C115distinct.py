def distinct(value):
    l = [0]*value
    for i in range(value):
        l[i] = int(input("Enter value: "))
    print(l)
    variable = l[0]
    commonArrayElements = []
    for k in range(0, value-1):
        if(l[k+1]==variable):
            commonArrayElements.append(variable)
            variable = l[k]
    print("List of common element in array")
    print(commonArrayElements)
distinct(5)
