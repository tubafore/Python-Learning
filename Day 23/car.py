from turtle import Turtle
from constants import *
import random

class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)

    def GetExtents(self) -> list[tuple[float,float]]:
        position = self.position()
        return [(position[0] - 20, position[1] + 10),(position[0] + 20, position[1] - 10)]