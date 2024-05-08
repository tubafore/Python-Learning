from turtle import Turtle
from constants import *

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.ResetPosition()

    def ResetPosition(self) -> None:
        self.teleport(0, STARTING_POSITION)

    def GetExtents(self) -> list[tuple[float,float]]:
        position = self.position()
        return [(position[0] - 9.5, position[1] + 12.5),(position[0] + 9.5, position[1] - 9.5)]
