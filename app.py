# this is a commment
"""
Python is a high-level programming language created by Guido van Rossum and first
released in 1991. Its reputation is growing, as today, various training institutes are
covering the language as part of their data science prospectus.
"""

"""
This is a multi-line string/ comment

"""

# VARIABLES: host references to something stored in memory
age = 12 # variable
name = "John Doe"
name = "Michael Angelo" # variable overriding
weight = 20.5
output =""  

 
"""
DATA TYPES:
    - NUMBERS: integers, float, complex
    - TEXT: strings str()
    - LIST:list, set, tuple, dictioary
"""

# integer: int()
numberOne = 20 # integer
output = type(numberOne) # checking the data type
 
numberTwo = 100000000000000
output = type(numberTwo)

output = numberOne
output = numberTwo

"""
ARITHMETIC OPERATORS:
    - addition(+)
    - subtraction(-)
    - multiplication(*)
    - division(/)
    - power(**)
    - floor division(//)
    - modulus(%)
"""
x = 10 
y = 12

output = x + y  # addition
output = x - y  # subtraction
output = x * y  # multiplication
output = x / y  # division
output = x // y # floor division => truncated
output = x % y  # modulus

x = 20 
y = 25
output = x // y

"""
ASSIGNMENT OPERATORS: 
    =, +=, *=, /=, **=, //=, %= 
  
"""

x = 10 
# x = x + 1 # addition
# x +=1 # same as  x = x-1
# x -= 1 # same as x = x-1
x *= 3 # same as x = x * 3
x /=3 # same as x = x / 3
x //=3 # same as x = x // 3
x **=3 # same as x = x ** 3
x %=3 # same as x = x % 3 

"""
COMPARISON OPERATORS: 
    - greater than(>)
    - less than (<)
    - less than or equal to (<=)
    - greater than or equal to (>=)
    - equal to (==)
    - not equal to (!=)
"""
x = 100
y = 90 

output = x < y # less than comparison
output = x > y # greater than
output = x <= y # less than or equal to comparison
output = x >= y # greater than or qual to comparison
output = x ==y # equality check
output = x != y # not equal to

"""
BOOLEAN OPERATORS: 
    - and 
    - or 
    - not
"""
fruit = "orange"
weather = "sunny"
output = (fruit == "orange") and (weather != "rainy") # true and false

age = 12
weight = 20.5

output = (age>18) and (weight<10) # false and false
output = (age<18) or (weight<10) # true or false => True
output = not ((age<18) or (weight<10)) # true or false => True

"""
STRINGS: 
    - list of characters
    -  surrounded by either '', "" or """ """
    - immutable 

"""

name ="@John#Doe"
output = name
output = type(name)
output = name[1] #accessing an element using index position
output = name[0:5] # slicing
# output = name[2:]
name = "Chronicals of Nania" 
output = name [1: 8: 3]# slice with a step

name = "Chronicals of Nania" 
output = name.upper() # string methods
output = name.lower()
output = name.find("Nania")
output = name[14:]
output = name.count("a")

name = "Chronicals"

location = "Nania"

output = name + location # string concatenation
location = "Nairobi"
output = f"{name} {location}" # f-string

output = "I am watching The "+name + " Of " + location
output = f"I am awatching The {name} or {location}"

name = "John Doe"
age = 12
hobby ="playing football"
home = "Nairobi"
school = "Emobilis"

output = "My name is "+name+". I am " +str(age)+" yrs old! I love "+hobby+"."+ "I school in "+school 
output = f"My name is {name} I am {age} yrs old! I love {hobby}I school in {school}"


"""
FUNCTIONS:
    - Do something(single purpsoe group of statements)
    - types: 
        - lambda function (anonymous function)
        - paramterized 
        - non parameterized 
"""
# lambda: params: expression

summation = lambda x,y,z : x+y+z
output = summation(2,3,5)

#  non-paramaterized functions: 
# defining a function
def greetings():
    print("Good afternoon World")

greetings() # calling a function


# defining the function
def checkWeather():
    print("The weather today is chilly!")


# call the function
checkWeather()





# HOUSE

def washDishes():
    print("tae soap")
    print("soak the dishes ")
    print("wash and rinse the dishes")


def morningRoutine():
    print("Get our of bed")
    print("brush my teeth")
    print("Drink water")
    print("read a book")
    print("do chores")
    print("REST!")

def prepareEggs():
    print("crack 2 eggs")
    print("separate the yolk")
    print("warm the pan")  
    print("pour tea spoon of cooking oil")  
    print("preprare the egg yolk for 3 min on both sides")
    print("EAT!")    

# calling the function
prepareEggs()

# parametrized function








print("==================")
print(output) # standard output
print("==================")

