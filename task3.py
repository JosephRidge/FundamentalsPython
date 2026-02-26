"""
Task 3: String Handling (10 min)

Take a string input

Print:
    Number of characters
    Number of vowels

Check if the string is a palindrome
"""

# name = input("Enter a your full name: ") # get input from user
# lengthOfWord = len(name) # get number of letters/ characters

 
# wordOfTheDay = "Courage"
# count = 0
# for letter in wordOfTheDay: 
#     match(letter):
#         case 'a': 
#             count +=1
#         case 'e':
#             count +=1
#         case 'i':
#             count +=1
#         case 'o':
#             count +=1
#         case 'u':
#             count +=1
#         case _:
#             print("not a vowel")

# print(f" I have {count} vowels")


"""
Task 3: String Handling (10 min)

Take a string input

Print:
    Number of characters
    Number of vowels

Check if the string is a palindrome
"""

userInput = input("Enter a word: ")
lengthOfCharacters = len(userInput)
output = f"WORD: {userInput} and NumberOfCharacters: {lengthOfCharacters}"
# print(output)


#  vowels: =. a,e,i, o ,u 

vowels= ["a","e","i","o","u"]
vowelCount = 0
for letter in userInput:
    if(letter.lower() in vowels):
        vowelCount += 1
    else:
        pass


vowelCount = 0

for letter in userInput:
    match(letter.lower()):
        case "a":
            vowelCount+=1
        case "e":
            vowelCount+=1
        case "i":
            vowelCount+=1
        case "o":
            vowelCount+=1
        case "u":
            vowelCount+=1
        case _:
            pass

# print(f"{userInput} has {vowelCount} vowels")

# check if word is palindrome 
if(userInput.lower() == userInput[::-1].lower()):
    print("Its a palindrome!")
else:
    print("Try again!")