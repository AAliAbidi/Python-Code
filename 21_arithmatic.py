def add(a,b):
    print("Adding %d + %d" %(a,b))
    return a + b
def sub(a,b):
    print("Subtraction %d + %d" %(a,b))
    return a - b
def mul(a,b):
    print("Multiplication %d + %d" %(a,b))
    return a * b
def div(a,b):
    print("Division %d + %d" %(a,b))
    return a / b

print("Let's do some math with just function!")

age = add(20, 3)
height = sub(78, 4)
weight = mul(90, 2)
iq = div(100, 2)

print("Age = %d, Height = %d, Weight = %d, IQ = %d" %(age, height, weight, iq))


