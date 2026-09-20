# Task 5: Loops
# This program demonstrates for loop and while loop.

# 1. Print numbers from 1 to 20 using a for loop
print("Numbers from 1 to 20:")

for number in range(1, 21):
    print(number, end=" ")

print("\n")


# 2. Print the multiplication table of a number
table_number = int(input("Enter a number for multiplication table: "))

print("\nMultiplication Table of", table_number)

for i in range(1, 11):
    print(table_number, "x", i, "=", table_number * i)

print()


# 3. Print even numbers from 1 to 50 using a while loop
print("Even numbers from 1 to 50:")

number = 2

while number <= 50:
    print(number, end=" ")
    number += 2