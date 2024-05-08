from turtle import Turtle, _Screen
from drawingHelper import DrawingHelper
from constants import *

class GameBoard:
    def __init__(self, screen:_Screen) -> None:
        self.turtle = Turtle()
        self.screen = screen
        self.turtle.color("white")
        self.turtle.teleport(BLOCK_SIZE / -2, (self.screen.window_height() - BLOCK_SIZE) / 2 + 5)
        self.turtle.setheading(270)
        self.turtle.hideturtle()
        self.setup()
    
    def setup(self) -> None:
        turtle = self.turtle
        turtle.fillcolor("white")
        turtle.setheading(270)
        while self.turtle.ycor() > (BLOCK_SIZE + (self.screen.window_height() / -2)):
            DrawingHelper.DrawRectange(turtle, BLOCK_SIZE, BLOCK_SIZE)
            turtle.teleport(BLOCK_SIZE / -2, turtle.ycor() - 2 * BLOCK_SIZE)