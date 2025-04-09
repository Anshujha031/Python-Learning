class Student:
    def __init__(self ,name):
        self.name = name

s = Student("Naveen")
print(s.name)
del s.name
print(s.name)

