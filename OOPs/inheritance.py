#---------Multilevel Inheritance--------------------
'''
class Car:
    @staticmethod
    def start():
        print("Car has started")
        
    @staticmethod
    def stop():
        print("car stopped!")

class ToyotaCar(Car):
    def __init__(self,brand):
      self.name = brand


class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
'''

#---------Multiple Inheritance-------------
'''
class A:
    varA = "Welcome tp class A"

class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "WElcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
'''
 #===========================================

class Car:
    def __init__(self,type):
        self.type = type


    @staticmethod
    def start():
        print("Car has started")
        
    @staticmethod
    def stop():
        print("car stopped!")

class ToyotaCar(Car):
    def __init__(self,name,type):
      self.name = name
      super().__init__(type)

# c = Car("Good")

car1 = ToyotaCar("perius","good")
print(car1.type)