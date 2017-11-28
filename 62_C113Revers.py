def orignalArray(value):
    #PRINTING ARRAY OF DESIRED RANGE

    l = [0]*value
    for i in range(value):
        l[i] = int(input("Enter Value: "))
    print("O   rignal array is:")
    print(l)

    #REVERSE PROGRAMING LOGIC
    Rev = l[::-1]
    print("Reverse Array is: ")
    print(Rev)
    #for k in range(-1, -5):
     #   revArray.append(k)
#    print ("Reverse array is: ")
 #   print(revArray)
orignalArray(5)
