from turtle import Turtle
from constants import *
from drawingHelper import DrawingHelper

class Paddle(Turtle):
    def __init__(self, x:int, y:int) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.teleport(x, y)
        self.color("white")
        self.height = PADDLE_HEIGHT
        self.width = BLOCK_SIZE


        

