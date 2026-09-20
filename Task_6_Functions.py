# Task 6: Functions
# This program demonstrates user-defined functions in Python.


# Function to calculate the square of a number
def calculate_square(number):
    return number * number


# Function to calculate the average of three numbers
def calculate_average(first, second, third):
    return (first + second + third) / 3


# Taking input from the user
number = float(input("Enter a number to find its square: "))

first_number = float(input("Enter the first number for average: "))
second_number = float(input("Enter the second number for average: "))
third_number = float(input("Enter the third number for average: "))


# Calling the functions
square = calculate_square(number)
average = calculate_average(first_number, second_number, third_number)


# Displaying the results
print("\n----- Results -----")
print("Square of", number, ":", square)
print("Average of the three numbers:", average)