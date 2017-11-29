num = int(input("Enter Number: "))
fact = 1
if num< 0:
    print("Number must be positive:")
if num == 0:
    print("Fibonacci is 1")
if num>0:
    for i in range(1, num+1):
        fact *= i
    print("Fibonacci is :\n%d\n"%fact)