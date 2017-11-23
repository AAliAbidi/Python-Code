class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Students("Fred", 17)
student2 = Students("Mike", 12)
print(hasattr(student1, "age"))
print(hasattr(student1, "grade"))
setattr(student1, 'grade', "8th")

print(student1.name)
print(student1.age)
print(student1.grade)

print(getattr(student2,"age"))

#delattr(student1,"grade")
