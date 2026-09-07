print("===== Student Result Management System =====")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))
computer = int(input("Enter Computer Marks: "))
hindi = int(input("Enter Hindi Marks: "))

print("\nStudent Details")
print("Name:", name)
print("Roll Number:", roll_no)

print("\nStudent Marks")
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Computer:", computer)
print("Hindi:", hindi)

# Total and Percentage

total = maths + science + english + computer + hindi
percentage = total / 5


# Grade Calculation

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "FAIL"

print("\nResult")
print("Total Marks :", total)
print(f"Percentage : {percentage:.2f}%")
print("Grade :", grade)