EnterNumber = int(input("Enter Your Number Greater then 1: "))
if EnterNumber > 1:
    for i in range(2, EnterNumber):
        if EnterNumber%i == 0:
            print("%d Number is not Prime" %(EnterNumber))
            break
    else:
        print("%d Number is prime" %(EnterNumber))
