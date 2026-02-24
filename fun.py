weather = "Cloudy" # global variable

def student(name, age, course):
    studentID = f"{name}{age}{course}" #local varible 
    print(f"Student is called: {name} and is {age} years old currently studying {course}")
    print(f"Student ID: {studentID}")

student("Ken", 12,"Coloring")
 



"""
FUNCTION: 
 -  does something(single purpose)

 Types:
    - lambda 
    - paramterized 
    - non-parameterized 

"""

# lambda => anonymous function 

stringNumber = lambda x: str(x)
output = stringNumber(100)
output = type(output)

ouput = type(stringNumber(100))
output = 100
output = type(output)
output = 100
output = f"{stringNumber(output)} type: {type(stringNumber(output))}"

# non-parametrized function
def greetings():
    print("Good evening!")
# greetings()

# parametrized function
def welcomeGreetings(firstName, lastName):
    print(f"Welcome {firstName} {lastName}, to @Emobilis")

def calculatMatrix():
    pass

calculatMatrix()
# welcomeGreetings("John", "Kamau")
# welcomeGreetings("Mary", "waKamau")
# welcomeGreetings("Peter", "lee Kamau")
# welcomeGreetings("Paul", "goo Kamau")
# welcomeGreetings("Martha", "hii Kamau")



print("==================")
# print(output)
print("==================")