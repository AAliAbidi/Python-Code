num = int(input("Enter Number: "))
fact = 1
if num< 0:
    print("Number must be positive:")
if num == 0:
    print("Factorial is 1")
if num>0:
    for i in range(1, num+1):
        fact *= i
    print("Factorial is :\n%d\n"%fact)
