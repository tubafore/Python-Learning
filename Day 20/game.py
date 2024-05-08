from turtle import Screen
from snake import Snake
from directions import *
from food import Food
from scoreboard import ScoreBoard
import time

class SnakeGame:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        #turn off animation updates
        #have to call update() ourselves
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.gameRunning = False
        self.score = 0
        self.scoreBoard = ScoreBoard()
        self.changingDirection = False
        self.setupKeybindings()

    def setupKeybindings(self) ->None:
        #tell the thing to listen to key presses
        self.screen.listen()
        self.screen.onkeypress(self.TurnUp, "Up")
        self.screen.onkeypress(self.TurnDown, "Down")
        self.screen.onkeypress(self.TurnLeft, "Left")
        self.screen.onkeypress(self.TurnRight, "Right")
        self.screen.onkeyrelease(self.Quit, "Escape")

    def TurnLeft(self) -> None:
        if self.snake.Head().heading() != RIGHT and not self.changingDirection:
            self.changingDirection = True
            self.snake.Head().setheading(LEFT)

    def TurnRight(self) -> None:
        if self.snake.Head().heading() != LEFT and not self.changingDirection:
            self.changingDirection = True
            self.snake.Head().setheading(RIGHT)

    def TurnUp(self) -> None:
        if self.snake.Head().heading() != DOWN and not self.changingDirection:
            self.changingDirection = True
            self.snake.Head().setheading(UP)

    def TurnDown(self) -> None:
        if self.snake.Head().heading() != UP and not self.changingDirection:
            self.changingDirection = True
            self.snake.Head().setheading(DOWN)

    def Quit(self) -> None:
        self.gameRunning = False
        self.screen.bye()

    def Run(self) -> None:
        # self.screen.update()
        self.gameRunning = True
        while self.gameRunning:
            self.snake.Move()
            self.scoreBoard.ShowScore(self.score)
            self._collisionCheck()
            self.screen.update()
            self.changingDirection = False
            time.sleep(0.1)
        self.scoreBoard.ShowGameOver()
        self.screen.exitonclick()

    def _collisionCheck(self):
        #check edges of the screen
        headPosition = self.snake.Head().position()
        screenWidth = self.screen.window_width()
        screenHeight = self.screen.window_height()
        if headPosition[0] > (screenWidth - self.snake.SnakeSize) / 2 or headPosition[0] < (-screenWidth + self.snake.SnakeSize) / 2:
            self.gameRunning = False
        if headPosition[1] > (screenHeight - self.snake.SnakeSize) / 2 or headPosition[1] < (-screenHeight + self.snake.SnakeSize) / 2:
            self.gameRunning = False

        #check hitting any body segment
        #slice the snake body by taking all but the first one
        for segment in self.snake.Body[1:]:
            if self.snake.Head().distance(segment.position()) <= 5:
                self.gameRunning = False
        
        if self.food.distance(headPosition) < 15:
            self.score += 1
            self.snake._addBodySegment()
            self.food.RefreshPosition()

        return False
        
    