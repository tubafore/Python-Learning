from turtle import Turtle, Screen
import random

class TurtleRace():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    def __init__(self, screen:Screen) -> None:
        self.screen = screen
        self.screen.setup(width=500, height=400)
        self.turtles = dict[str, Turtle]()
        self.choice = ""
        self.gameOver = False
        self.winners = []
        self.turtleWidth = 25

        #setup the new turtles for racing and put them in their spots
        #the complicated math is due to the origin being in the middle of the screen
        #it moves the turtle 20 pixels off the left edge, and spaces each turtle
        #1/6th down the screen from the previous one, starting 30 from the top
        for color in TurtleRace.colors:
            newTurtle = Turtle(shape="turtle")
            newTurtle.penup()
            newTurtle.color(color)
            newTurtle.teleport(-230, (self.screen.window_height() / 2 - 30) - (self.screen.window_height() / len(TurtleRace.colors)) * len(self.turtles))
            self.turtles[color] = newTurtle

    def Race(self):
        self.choice = self.screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

        while not self.gameOver:
            #move the turtles a random amount from 1 to 10
            for racer in self.turtles:
                self.turtles[racer].forward(random.randint(1, 10))

            #check their x-coordinate to see if it's at the edge of the screen (minus the width of the turtle)
            for racer in self.turtles:
                if self.turtles[racer].xcor() >= (self.screen.window_width() / 2) - self.turtleWidth:
                    self.gameOver |= True
                    self.winners.append(racer)
            
        if self.gameOver:
            if self.choice in self.winners:
                print("You win!")
            else:
                print("You lose.")
            if len(self.winners) == 1:
                print(f"The winning color was {self.winners[0]}")
            else:
                print(f"The winning colors were {" and ".join(self.winners)}")


