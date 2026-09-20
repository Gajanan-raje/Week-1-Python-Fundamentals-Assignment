# Task 4: Conditional Statements
# This program calculates the grade based on marks.

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\n----- Result -----")
print("Marks:", marks)
print("Grade:", grade)