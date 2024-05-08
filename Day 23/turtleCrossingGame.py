from turtle import Screen
from carManager import *
from player import *
import time

from scoreboard import Scoreboard


class TurtleCrossingGame():
    def __init__(self) -> None:
        self.screen = Screen()
        self.SetupScreen()
        self.gameIsRunning = False
        self.CarManager = CarManager(self.screen)
        self.Level = 1
        self.Scoreboard = Scoreboard()
        self.Scoreboard.Draw(self.Level)
        self.Player = Player()

    def SetupScreen(self) -> None:
        self.screen.setup(width=600, height=600)
        self.screen.title("Turtle Crossing")
        self.screen.tracer(0)
        self.screen.onkeypress(self.MovePlayer, "Up")
        self.screen.onkey(self.Quit, "Escape")
        self.screen.listen()

    def MovePlayer(self) -> None:
        self.Player.forward(MOVE_DISTANCE)

    def Quit(self) -> None:
        self.screen.bye()

    def NextLevel(self) -> None:
        self.CarManager.Reset()
        self.Level += 1
        self.Scoreboard.Draw(self.Level)
        self.Player.ResetPosition()

    def Play(self) -> None:
        self.gameIsRunning = True
        while self.gameIsRunning:
            self.CarManager.MoveCars()
            self.screen.update()
            if self.CarManager.CheckForCollisions(self.Player):
                self.gameIsRunning = False

            elif self.Player.ycor() >= self.screen.window_height() / 2 - 12.5:
                self.NextLevel()

            time.sleep(0.1)
        self.Scoreboard.DrawGameOver()
        self.screen.exitonclick()