"""
Object Oriented Programming: 
    - programming paradigm that aids in code reusability through classes and objects. 
"""

class Bottle:
    # attibutes
    company = "Emobi-Water"
    year = 2026
    color ="blue"
    size = 500

    # methods
    def drinkWater(self):
        print("drinking water")
    
    def getDetails(self):
        print(f"founded by {company}")


# dasaniBottle = Bottle()
class Hobby:
    #  attributes
    name = "Football"
    category = "Physical"
    frequency =  5

    #  methods
    def kickBall(self):
        print("kicking the ball")

    def startGame(self):
        print("Whistle has been blown!")


# footballGame = Hobby() # object

# footballGame.kickBall() 


class Matatu:
    #  attributes
    name = "Beast"
    color = "indigo"
    hasMusic = True
    size = 24

    #  methods
    def describeMatatu(self):
        print(f"Matatu {self.name}, is of color {self.color} and of a {self.size} seater ")

    def driving(self):
        print("matatu is being driven")


matatuOne = Matatu() # object
matatuOne.driving()
matatuOne.describeMatatu()