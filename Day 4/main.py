#using statements
#these are called modules in python
#importing from a file in your project is done by the name of the file without the .py
import random
from assignment import PaperRockScissorsGame

def randomPractice():
    print(random.randint(1, 10))
    #how to get a random number between 0 (inclusive) and 5 (exclusive)
    print(random.random() * 5)

def coinFlip():
    if random.randint(0, 1) == 1:
        print("Heads")
    else:
        print("Tails")

#Lists time
#declared with []
def listNotes():
    states = ["Delaware", "Pennsylvania", "New Jersey"] #etc. etc.
    #access an item with [] just like c#
    #0-indexed
    print(states[0]) 
    #accessing an item from the end of a list
    #using negative indices
    #here's the last item
    print(states[-1])
    #add an item to the end of the list
    states.append("Georgia")
    #add a bunch of items to the end of the list
    states.extend(["Alabama", "Alaska", "Arkansas"])

def foodBill():
    names_string = "Angela, Ben, Jenny, Michael, Chloe"
    names = names_string.split(", ")
    #get the length of the list with len(listName)
    #it's not a property of the list itself
    print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")

#nested lists
def nestedLists():
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

    #lists within lists!
    dirtyDozen = [fruits, vegetables]
    #can't be accessed by name after insertion. ex: no dirtyDozen.fruits[0]
    #instead it's just a two dimensional list now
    print(dirtyDozen[0][0])

def treasureMap():
    #their code
    line1 = ["","",""]
    line2 = ["","",""]
    line3 = ["","",""]
    map = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")
    position = input() # Where do you want to put the treasure?

    #my code
    characters = [position[0].lower(), position[1]]
    #ord() gets the unicode value of a character
    column = ord(characters[0]) - ord('a')
    row = int(characters[1]) - 1
    map[row][column] = 'X'

    #their code
    print(f"{line1}\n{line2}\n{line3}")

PaperRockScissorsGame.Game()

