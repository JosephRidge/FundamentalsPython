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
    def __init__(self, name, color, hasMusic, size):
        self.name = name 
        self.color = color 
        self.hasMusic = hasMusic
        self.size = size

    #  methods
    def describeMatatu(self):
        return f"Matatu {self.name}, is of color {self.color} and of a {self.size} seater "

    def driving(self):
        print("matatu is being driven")

matatuWestlands = Matatu("M3Westland","blue",False,48) # object
# matatuWestlands.driving()
# matatuWestlands.describeMatatu()

# print("=====================================")
matatuCBD = Matatu("M3CBD","green", False, 12)
# matatuCBD.driving()
output = matatuCBD.describeMatatu() 
# print(output)


"""
INHERITANCE: 
  - parent and a child. The child inherits
   behaviors & attributes of the parent
"""

class Vehicle: 

    def __init__(self, name, color, model, yom):
        self.name = name
        self.color = color
        self.yom = yom 
        self.model = model 

    def drive(self):
        print(f"I am driving my {self.model} and I call it {self.name}")

    def hoot(self):
        print("Hoot Hoot!")

class Tuktuk(Vehicle):
    pass 

# tuktukNairobi = Tuktuk("RedSparrow", "red","toyota",2026)
# tuktukNairobi.hoot()

class Shoe:
    def __init__(self, name, brand, purpose):
        self.name = name
        self.brand = brand
        self.__purpose = purpose 

    def walk(self):
        print("I am walking")
    
    def decribeShoe(self):
        print(f"This shoe is of brand: {self.brand}")
        print(f"This shoe is called: {self.name}")
        print(f"This shoe is for: {self.purpose}")


class RunningShoes(Shoe):
    pass 

nike = RunningShoes("walkers", "Nike", "running")

nike.decribeShoe()
print(nike.name)
print(nike.brand)
print(nike.purpose)