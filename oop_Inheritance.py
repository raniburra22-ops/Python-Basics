#Multi-level Inheritance
class Car :
    @staticmethod #decorator that do not use self parameter
    def start() :
        print("Car Started...")

    @staticmethod 
    def stop():
        print("Car Stopped... ")

class ToyotaCar(Car) :
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar) :
    def __init__(self, type):
        self.type = type

c1 = Fortuner("Diesel")
c1.start()
print(c1.type)

#Multiple Inheritance

class A:
    varA = "Wellcome to class A"

class B:
    varB = "Wellcome to class B"

class C(A, B):
    varC = "Wellcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)