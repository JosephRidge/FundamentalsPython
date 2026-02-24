"""
LISTS: 
    - lists
    - sets
    - tuples
    - dictionary
"""

fruits = ["apple", "mango", "bananas", 2,3, 4.56] #list
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


print("===========================")
print(output)
print("===========================")