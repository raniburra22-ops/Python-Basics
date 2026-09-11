#Class & Object
#Creating Class
class Car :
    color = "Black"
    brand = "Mercedes"
c1 = Car()
print(c1.color)
print(c1.brand)

#__init__ Fuction
#Constructor
class Student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in database.")
s1 = Student("Ansh", 98 )
print(s1.name, s1.marks)
s2 = Student("Akshanshuh", 99)
print(s2.name, s2.marks)

#class & Instance Attributes
class Students :
    college_name = "ABC college"
    def __init__(self, names, mark):
        self.names = names
        self.mark = mark
s3 = Students("karan", 98)
print(s3.names, s3.mark)
print(s3.college_name)