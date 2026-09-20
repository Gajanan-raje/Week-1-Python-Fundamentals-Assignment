# Task 9: Student Record Management System
# This program allows the user to add, display, search,
# and delete student records.

student_records = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    branch = input("Enter student branch: ")
    marks = float(input("Enter student marks: "))

    student = {
        "Name": name,
        "Age": age,
        "Branch": branch,
        "Marks": marks
    }

    student_records.append(student)
    print("Student record added successfully.")


def display_students():
    if len(student_records) == 0:
        print("No student records available.")
        return

    print("\n----- Student Records -----")

    for student in student_records:
        print("Name  :", student["Name"])
        print("Age   :", student["Age"])
        print("Branch:", student["Branch"])
        print("Marks :", student["Marks"])
        print("--------------------------")


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in student_records:
        if student["Name"].lower() == search_name.lower():
            print("\nStudent found!")
            print("Name  :", student["Name"])
            print("Age   :", student["Age"])
            print("Branch:", student["Branch"])
            print("Marks :", student["Marks"])
            found = True
            break

    if not found:
        print("Student record not found.")


def delete_student():
    delete_name = input("Enter student name to delete: ")

    for student in student_records:
        if student["Name"].lower() == delete_name.lower():
            student_records.remove(student)
            print("Student record deleted successfully.")
            return

    print("Student record not found.")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the Student Record Management System.")
        break

    else:
        print("Invalid choice. Please try again.")