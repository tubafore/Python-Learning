from turtle import Turtle
from constants import *

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.teleport(-280, 260)
        self.penup()
        self.hideturtle()

    def Draw(self, level:int) -> None:
        self.clear()
        self.write(f"Level: {level}", font=FONT)

    def DrawGameOver(self) -> None:
        self.teleport(0,0)
        self.write("Game Over".upper(), align="center", font=FONT)