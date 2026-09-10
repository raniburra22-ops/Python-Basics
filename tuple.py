#Python Tuple Basics
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Print length of Tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) 

#Tuple Methods
tup = (1, 2, 3, 2, 4, 2)
print(tup.index(2))
print(tup.count(2))

#WAP to count the number of student with the "A" grade in the tuple
tupl = ("A", "D", "A", "B", "B", "C")
print(tupl.count("A"))

#Tuple with For Loop
marks = (78, 85, 90, 67, 88, )
print("Marks :")

for mark in marks :
    print(mark)

print("Highest Marks :", max(marks))
print("Lowest Marks :", min(marks))
print("Total Marks :", sum(marks))
print("Number of Subject :", len(marks))


