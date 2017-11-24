def bufferSize(var):
    l = [0]*var
    for i in range(var):
        l[i] = int(input("Enter value: "))
    print("Orignam Array\n", l)

    #Accessing Out Bound Array Elements
    try:
        print(l[var+1])
    except:
        print("Exception Caught, Don’t try buffer overflow attacks in Python!")


bufferSize(5)
