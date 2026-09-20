# Task 8: Basic File Handling
# This program creates a text file, writes information into it,
# and reads the contents of the file.


introduction = """Hello, my name is Gajanan Raje.
I am a BCA student.
I am interested in Python and Data Analytics.
I am currently learning Python programming and data analysis."""


# Creating and writing to a text file
with open("introduction.txt", "w") as file:
    file.write(introduction)


# Reading the contents of the file
with open("introduction.txt", "r") as file:
    content = file.read()


print("----- File Contents -----")
print(content)