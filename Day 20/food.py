from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.RefreshPosition()

    def RefreshPosition(self) -> None:
        xPosition = random.randint(-14, 14)*20
        yPosition = random.randint(-14, 14)*20

        self.setposition((xPosition, yPosition))