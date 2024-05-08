#like usual
from turtle import Turtle, Screen
from assignment import TurtleRace

# tim = Turtle()
# tim.speed("fastest")
# screen = Screen()

# '''Etch-A-Sketch Code'''
# def moveForward(turtle:Turtle, distance:int = 10):
#     turtle.forward(distance)

# def moveBackward(turtle:Turtle, distance:int = 10):
#     turtle.backward(distance)

# def turnRight(turtle:Turtle, rate:int = 5):
#     turtle.right(rate)

# def turnLeft(turtle:Turtle, rate:int = 5):
#     turtle.left(rate)

# def clear(turtle:Turtle):
#     #turtle.clear()
#     #turtle.home()
#     turtle.reset()

# def moveTimForward():
#     moveForward(tim, 10)

# def moveTimBackward():
#     moveBackward(tim, 10)

# def turnTimRight():
#     turnRight(tim, 5)

# def turnTimLeft():
#     turnLeft(tim, 5)

# def cleanUpAfterTim():
#     clear(tim)

#setup the screen to listen for events
# screen.listen()
#binding a listener to the space key
#onkey seems to be on key UP
# screen.onkeypress(key="w", fun=moveTimForward)
# screen.onkeypress(key="a", fun=turnTimLeft)
# screen.onkeypress(key="s", fun=moveTimBackward)
# screen.onkeypress(key="d", fun=turnTimRight)
# screen.onkeypress(key="c", fun=cleanUpAfterTim)

#python refers to passing functions as arguments as "Higher Order Functions"

race = TurtleRace(Screen())
race.Race()

race.screen.exitonclick()