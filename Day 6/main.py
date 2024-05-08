#officially learning functions this time
#always starts with def, no return type given
#after the name and (arguments in parentheses)
#end with a colon, like everything else in python
#remember that indentation is important in python and maintains
#the scope until you unindent out of the scope
def myFunction():
    print("Hello")
    print("Bye")

#coding challenges on https://reeborg.ca today
#this is a backup of what I do there

#pretending these functions exist
#pass just tells the compiler it's not implemented
def turn_left():
    pass
def move():
    pass
def at_goal():
    pass
def front_is_clear():
    pass
def right_is_clear():
    pass
#end pretend functions

def turnLeft():
    turn_left()

def turnAround():
    turn_left()
    turn_left()
    
def turnRight():
    turnAround()
    turn_left()

def makeSquare():
    turnLeft()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turnRight()
    move()

def jumpHurdle():
    turnLeft()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turnLeft()

#Hurdle 1 solution
#range(6) is equivalent to range(0,6)
for i in range(0, 6):
    move()
    jumpHurdle()

#Hurdle 2 solution
#no ! operator, use the word not
while not at_goal():
    move()
    jumpHurdle()

#Hurdle 3 solution
while not at_goal():
    while front_is_clear():
        move()
    jumpHurdle()

#Hurdle 4 solution
def jumpVariableHeightHurdle():
    turnLeft()
    #jump up
    while not right_is_clear():
        move()
    #move over hurdle
    turnRight()
    move()
    turnRight()
    move()
    #jump down
    while not right_is_clear() and front_is_clear():
        move()
    turnLeft()

while not at_goal():
    while front_is_clear() and not at_goal():
        move()
    if not at_goal():
        jumpVariableHeightHurdle()

#Maze Solution
#there is still an edge case
while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    elif right_is_clear():
        turnRight()
        move()
    elif front_is_clear():
        move()
    else:
        turnLeft()