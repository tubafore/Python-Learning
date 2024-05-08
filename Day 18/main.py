#import notes
# import turtle #imports the whole module, you reference things in it with turtle.ClassName

#import a single class from the module, referenced by ClassName
from turtle import Turtle
from turtle import Screen
import random
from assignment import HirstPaintingGenerator

# from turtle import * #import everything from the module and reference EVERY class by its ClassName within the module

# import turtle as t #imports the whole module, you reference it with t.ClassName where "t" is the name you specify after the "as"

def drawDashedLine(turtle:Turtle, totalLength:int, dashLength:int):
    for i in range(0, totalLength, 2 * dashLength):
        turtle.forward(dashLength)
        turtle.penup()
        turtle.forward(dashLength)
        turtle.pendown()

def generateRandomColorString() -> str:
    #generate a random 24-bit number
    color = random.randint(0, 2**24-1)
    #format the number in a 6-digit hex string preceded by a "#"
    return "#{:06x}".format(color)

def generateRandomColor() -> tuple[int, int, int]:
    """must call screen.colormode(255) for this to work"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def drawNGon(turtle:Turtle, sides:int):
    angle = 360 / sides
    turtle.color(generateRandomColorString())
    for i in range(sides):
        turtle.forward(100)
        turtle.right(angle)

def drawSquare(turtle:Turtle):
    drawNGon(turtle, 4)

def drawAllThePolygons(turtle:Turtle):
    for i in range(4, 13):
        drawNGon(turtle, i)

def randomWalk(turtle:Turtle, screen:Screen, stride:int, numberOfStrides:int = 200):
    screen.colormode(255)
    turtle.pensize(8)
    turtle.speed("fastest")
    directions = [0, 90, 180, 270]
    for _ in range(numberOfStrides):
        #turtle.color(generateRandomColorString())
        turtle.color(generateRandomColor())
        #without turning, just set the direction
        turtle.setheading(random.choice(directions))
        turtle.forward(stride)

def spiroGraph(turtle:Turtle, numberOfCirlces:int = 100):
    turtle.speed("fastest")
    for i in range(numberOfCirlces):
        turtle.color(generateRandomColorString())
        turtle.setheading(i * 360 / numberOfCirlces)
        turtle.circle(200)

timmy = Turtle()
screen = Screen()
#drawSquare(timmy)
#drawDashedLine(timmy, 500, 10)
drawAllThePolygons(timmy)
#randomWalk(timmy, screen, 20)
# spiroGraph(timmy)


# paintingGenerator = HirstPaintingGenerator(timmy, screen)
# paintingGenerator.Run(50, 10, 10, 30)

screen.exitonclick()