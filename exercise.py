"""
Exercise: 
1. Calculate and print the sum and average of all numbers in a list.
Given:
my_list = [10, 20, 30, 40, 50]
total = sum(my_list)

2. Reverse a list
Given: list1 = [100, 200, 300, 400, 500]

3. Write a function that takes a list with duplicate elements and returns a new list with only unique elements.
Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
Expected Output:[1, 2, 3, 4, 5]

"""

"""
1. Calculate and print the sum and average of all numbers in a list.
Given:
my_list = [10, 20, 30, 40, 50] 
"""
my_list = [10, 20, 30, 40, 50]
total = sum(my_list)
average = total/len(my_list)

"""
2. Reverse a list
Given: list1 = [100, 200, 300, 400, 500]
"""
list1 = [100, 200, 300, 400, 500]
list1.reverse()

"""
Write a function that takes a list with duplicate elements and returns a new list with only unique elements.
Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
Expected Output:[1, 2, 3, 4, 5] 
"""
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

list_without_duplicates = set(list_with_duplicates)

# print("--------------------------")
# print(f"AVG: {average}")
# print(f"SUM: {total}")
# print(f"reversed list: {list1}")
# print(f"list_without_duplicates: {list_without_duplicates}")
# print("--------------------------")


"""
 Calculate and print the sum and average of all numbers in a list.
Given:
my_list = [10, 20, 30, 40, 50]
total = sum(my_list)
"""

my_list = [10, 20, 30, 40, 50]
total = 0

for num in my_list:
    total += num

def calculateTotal(listOfNumbers):
    total = 0
    for num in my_list:
        total += num
    return total

result  = calculateTotal(my_list)

result = lambda x : sum(x)
total = result(my_list)
average = total/ len(my_list)

reverse = lambda l : l.reverse()
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
reverse(list_with_duplicates)
print(list_with_duplicates) 