#Python List Basics
studnts = ["Nabah", "Siya", "Neelam", "Neha"]

print("Student :", studnts)
print("First Student :", studnts[0])
print("Last Student :", studnts[-1])

studnts.append("Pooja")
print("After append :", studnts)

studnts.remove("Neha")
print("After remove :", studnts)

studnts.sort()
print("After sort : ", studnts)

studnts.reverse()
print("After reverse :", studnts)

print("Number of Student :", len(studnts))

#List with For Loop
marks = [78, 97, 86, 75, 68]

print("Student Marks :")
for mark in marks:
    print(mark)

total = 0

for mark in marks:
    total = total+mark

print("Total Marks :", total)
print("Average Marks :", total/len(marks)) 