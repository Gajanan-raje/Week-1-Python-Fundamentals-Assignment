# Task 7: Strings and Collections
# This program demonstrates strings, lists, tuples, dictionaries, and sets.


# 1. String Operations
print("----- String Operations -----")

text = "Python Data Analytics"

print("Original String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("After Replace:", text.replace("Python", "Advanced Python"))
print("Position of 'Data':", text.find("Data"))


# 2. List Operations
print("\n----- List Operations -----")

subjects = ["Python", "SQL", "Power BI"]

print("Original List:", subjects)

subjects.append("Excel")
print("After append():", subjects)

subjects.remove("SQL")
print("After remove():", subjects)

subjects.sort()
print("After sort():", subjects)


# 3. Tuple Creation and Indexing
print("\n----- Tuple Operations -----")

student_details = ("Gajanan", "BCA", 2027)

print("Tuple:", student_details)
print("First item:", student_details[0])
print("Second item:", student_details[1])


# 4. Dictionary
print("\n----- Dictionary Operations -----")

student = {
    "Name": "Gajanan",
    "Branch": "BCA",
    "Year": 3
}

print("Student Information:")

for key, value in student.items():
    print(key, ":", value)


# 5. Set Operations
print("\n----- Set Operations -----")

skills = {"Python", "SQL", "Power BI"}

print("Original Set:", skills)

skills.add("Excel")
print("After add():", skills)

skills.remove("SQL")
print("After remove():", skills)