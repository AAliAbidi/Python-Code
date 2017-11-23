def array(size):
    l = [0]*size
    k = [0]*size
    #ELEMENTS FOR FIRST ARRAY
    print("Enter 5 elements of your choice \n")
    for i in range(size):
        l[i] = int(input("Enter number: "))
    print("\nFirst Array is:")
    print(l)
    #TAKING ELEMENTS FOR SECOND ARRAY
    print("\nEnter 5 elements of your choice again for second array")
    for x in range(size):
        k[x] = int(input("Enter number: "))
    print("\nSecond Array is:")
    print(k)
    cp = [] #Empty Array to store cross product
    for m in range(0, size-1):
        for n in range(0, size-1):
            cp.append(l[n]*k[n])
    print(cp)



array(5)
