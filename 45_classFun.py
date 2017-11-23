class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayStudent(self):
        print("Student name is "+self.name+"and age is "+str(self.age))

stu = Student("Chad", 15)
stu.displayStudent()
#print(stu.displayStudent())

