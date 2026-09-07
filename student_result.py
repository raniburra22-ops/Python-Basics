print("===== Student Result Management System =====")

#Student Details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

#Subject Marks
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))
computer = int(input("Enter Computer Marks: "))
hindi = int(input("Enter Hindi Marks: "))

# Total and Percentage
total = maths + science + english + computer + hindi
percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A"
elif percentage >= 75 and percentage < 90 :
    grade = "B"
elif percentage >= 60 and percentage <75 :
    grade = "C"
else:
    grade = "FAIL"

#Pass and fail
if maths >= 33 and science >= 33 and english >= 33 and computer >= 33 and hindi >= 33 :
    result = "PASS"
else :
    result = "FAIL"

#Output 
print("-------------------STUDENT REPORT CARD--------------------------")
print("\nStudent Details")
print("Name:", name)
print("Roll Number:", roll_no)

print("------------Marks--------------")
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Computer:", computer)
print("Hindi:", hindi)

print("--------------Result------------")
print("Total Marks : ", total, "/500" )
print(f"Percentage : { percentage: .2f}%")
print("Grade : ", grade)
print("Result :", result)

print("\nThank you for using Student Result Management System! ")




