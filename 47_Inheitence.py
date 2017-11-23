class Parent:
    counter = 10
    def __init__(self):
        print("Class Initialised")
    def parentFunction(self):
        print("Parent function being called")
    def setCounter(self, num):
        Parent.counter = num
    def showCounter(self):
        print(Parent.counter)

class child(Parent):
    def __init__(self):
        print("Child class being initalised")
    def childFun(self):
        print("Chiled fun being called")

c = child()
c.childFun()
c.parentFunction()
p = Parent()
print("Global Counter", p.counter)
c.showCounter()
c.setCounter(20)
c.showCounter()
p.setCounter(30)
p.showCounter()
