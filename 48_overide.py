class Parent:
    def func(self):
        print("This is parent function")

class child(Parent):
    def func(self):
        print("This is child function")

c = child()
c.func()    #overiding function

