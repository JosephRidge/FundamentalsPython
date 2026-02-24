"""
LISTS: 
    - lists
    - sets
    - tuples
    - dictionary
"""

fruits = ["apple", "mango", "bananas"] #list
output = fruits[1]
output = fruits[2]

# for loop
# for fruit in fruits:
#     print(fruit)


students = ["John", "Doe","Peter", "Martha", "Kome"]

for student in students:
    print(student)


for index, student in enumerate(students):
    print(f"{index + 1}. {student}")

output = type(students)

students = ["John", "Doe","Peter", "Martha", "Kome"]
students[0] = "Parker"
name = "Pete"
students[3] = "Maria"
output = students
# name[0] = "R"
colors = ["green","green", "green",  "blue", "blue","gray","purple","yellow"]
output = colors.count("green") # check how many times has "green" been repeated


# set: ==>
uniqueColors = {"green","green", "green",  "blue", "blue","gray","purple","yellow"}
output = uniqueColors
output = type(uniqueColors)

#  Dictionaries




print("===========================")
print(output)
print("===========================")