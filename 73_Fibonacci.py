rng = int(input("Print positive Range: "))
try:
    if(rng>0):
        firstNo = 0
        SecondNo= 1
        fiboSum = firstNo+SecondNo
        print ("%d\n%d\n%d"%(firstNo, SecondNo, fiboSum))
        for i in range(1, rng):
            firstNo = SecondNo
            SecondNo = fiboSum
            fiboSum = firstNo+SecondNo
            print(fiboSum)
except:
    print("Exception Caught")
