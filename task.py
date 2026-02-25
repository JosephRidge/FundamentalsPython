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

 
wordOfTheDay = "Courage"
count = 0
for letter in wordOfTheDay: 
    match(letter):
        case 'a': 
            count +=1
        case 'e':
            count +=1
        case 'i':
            count +=1
        case 'o':
            count +=1
        case 'u':
            count +=1
        case _:
            print("not a vowel")

print(f" I have {count} vowels")