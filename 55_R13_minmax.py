def minmax(data):
    l = [0]*data
    for i in range (data):
        l[i] = int(input("Enter Digit: "))
    print ("List is \n", l)
    max = l[0]
    min = l[0]
    for k in range(0, data-1):
        if(l[k+1]>max ):
            max = l[k+1]
        if(l[k+1]<min):
            min = l[k+1]

    
    print(max,min)
    #for k in (0, data-1):
     #   if(l[k]>l[k+1]):
      #      min = l[k]
       #     print(min)
minmax(5)
