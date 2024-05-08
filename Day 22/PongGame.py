from GameBoard import *
from Paddle import *
from turtle import Screen
from Ball import Ball
import random
import time
import math

from Scoreboard import Scoreboard

class PongGame:
    def __init__(self) -> None:
        self.gameRunning = False
        self.Player1Score = 0
        self.Player2Score = 0
        self.screen = Screen()
        self.setupScreen()
        self.GameBoard = GameBoard(self.screen)
        self.Scoreboard = Scoreboard()
        self.Player1Paddle = Paddle(int((self.screen.window_width() - PADDLE_HEIGHT) / -2), 0)
        self.Player2Paddle = Paddle(int((self.screen.window_width() - PADDLE_HEIGHT) / 2), 0)
        self.Ball = Ball()
        self.initializeBall()
        self.VelocityMultiplier = 1.1

    def setupScreen(self) -> None:
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.registerKeyListeners()
        self.screen.listen()    

    def initializeBall(self) -> None:
        self.Ball.clear()
        self.Ball.Colliding = False
        self.Ball.teleport(0,0)
        #we're getting 30% to 90% of the velocity going in the x direction
        xVelocity = BALL_SPEED * (random.randint(3, 9) / 10)
        #randomize the x direction
        xVelocity *= random.randrange(-1, 2, 2)
        yVelocity = math.sqrt(BALL_SPEED ** 2 - xVelocity ** 2)
        if random.randint(0, 1) == 1:
            yVelocity = -1 * yVelocity
        self.Ball.Velocity = (xVelocity, yVelocity)

    def registerKeyListeners(self) -> None:
        self.screen.onkeyrelease(self.Quit, "Escape")
        self.screen.onkeypress(self.Player1Up, "w")
        self.screen.onkeypress(self.Player1Down, "s")
        self.screen.onkeypress(self.Player2Up, "Up")
        self.screen.onkeypress(self.Player2Down, "Down")

    def PaddleUp(self, paddle:Paddle) -> None:
        if paddle.ycor() < self.screen.window_height()/2 - PADDLE_HEIGHT/2 :
            paddle.sety(paddle.ycor() + MOVEMENT_STEP)

    def PaddleDown(self, paddle:Paddle) -> None:
        if paddle.ycor() > self.screen.window_height() / -2 + PADDLE_HEIGHT/2:
            paddle.sety(paddle.ycor() - MOVEMENT_STEP)

    def Player1Up(self) -> None:
        self.PaddleUp(self.Player1Paddle)

    def Player1Down(self) -> None:
        self.PaddleDown(self.Player1Paddle)

    def Player2Up(self) -> None:
        self.PaddleUp(self.Player2Paddle)

    def Player2Down(self) -> None:
        self.PaddleDown(self.Player2Paddle)

    def Quit(self) -> None:
        self.gameRunning = False

    def ProcessBallPosition(self) -> None:
        ballPosition = self.Ball.position()
        #top left and bottom right points of the ball
        ballExtents = [(ballPosition[X] - BLOCK_SIZE / 2, ballPosition[Y] + BLOCK_SIZE /2),(ballPosition[X] + BLOCK_SIZE / 2, ballPosition[Y] - BLOCK_SIZE /2)]
        paddle1Position = self.Player1Paddle.position()
        paddle2Position = self.Player2Paddle.position()
        paddle1Extents = [(paddle1Position[X] - PADDLE_WIDTH /2, paddle1Position[Y] + PADDLE_HEIGHT / 2), (paddle1Position[X] + PADDLE_WIDTH / 2, paddle1Position[Y] - PADDLE_HEIGHT / 2)]
        paddle2Extents = [(paddle2Position[X] - PADDLE_WIDTH /2, paddle2Position[Y] + PADDLE_HEIGHT / 2), (paddle2Position[X] + PADDLE_WIDTH / 2, paddle2Position[Y] - PADDLE_HEIGHT / 2)]
        windowHeight = self.screen.window_height() / 2
        windowWidth = self.screen.window_width() / 2
        applyVelocity = True

        #check horizontal wall collision
        if ballExtents[TOP][Y] > windowHeight or ballExtents[BOTTOM][Y] < -windowHeight:
            self.Ball.reflectVelocity()
        #check for collision with paddle 1
        elif not self.Ball.Colliding and PongGame.DoExtentsCollide(ballExtents, paddle1Extents):
            self.Ball.Colliding = True
            #is it a top or bottom edge?
            if PongGame.DetectHorizontalEdgeCollision(ballExtents, paddle1Extents):
                self.Ball.reflectVelocity() 
            else:
                self.Ball.reflectVelocity(True)
            self.IncreaseVelocity()
        #check for collision with paddle 2
        elif not self.Ball.Colliding and PongGame.DoExtentsCollide(ballExtents, paddle2Extents):
            self.Ball.Colliding = True
            #is it a top or bottom edge?
            if PongGame.DetectHorizontalEdgeCollision(ballExtents, paddle2Extents):
                self.Ball.reflectVelocity() 
            else:
                self.Ball.reflectVelocity(True)
            self.IncreaseVelocity()
        elif self.Ball.Colliding and not (PongGame.DoExtentsCollide(ballExtents, paddle1Extents) or PongGame.DoExtentsCollide(ballExtents, paddle2Extents)):
            self.Ball.Colliding = False
        elif ballExtents[BOTTOM][X] >= windowWidth or ballExtents[TOP][X] <= -windowWidth:
            if ballPosition[X] > 0:
                self.Player1Score += 1
            else:
                self.Player2Score += 1
            self.UpdateScoreboard()
            self.initializeBall()
            applyVelocity = False

        if applyVelocity:
            self.Ball.teleport(ballPosition[X] + self.Ball.Velocity[X], ballPosition[Y] + self.Ball.Velocity[Y])

    def IncreaseVelocity(self) -> None:
        self.Ball.Velocity = (self.Ball.Velocity[0] * self.VelocityMultiplier, self.Ball.Velocity[1] * self.VelocityMultiplier)

    def UpdateScoreboard(self) -> None:
        self.Scoreboard.Draw(self.Player1Score, self.Player2Score)

    def DoExtentsCollide(first:list[tuple[float, float]], second:list[tuple[float, float]]) -> bool:
        if len(first) != 2 or len(second) != 2:
            raise Exception("Each argument must contain exactly 2 tuples")
        if (second[TOP][X] <= first[TOP][X] and first[TOP][X] <= second[BOTTOM][X]) or \
           (second[TOP][X] <= first[BOTTOM][X] and first[BOTTOM][X] <= second[BOTTOM][X]):
            if (second[BOTTOM][Y] <= first[TOP][Y] and first[TOP][Y] <= second[TOP][Y]) or \
               (second[BOTTOM][Y] <= first[BOTTOM][Y] and first[BOTTOM][Y] <= second[TOP][Y]):
                return True
        return False
    
    def DetectHorizontalEdgeCollision(ballExtents:list[tuple[float,float]], paddleExtents:list[tuple[float,float]]) -> bool:
        return (ballExtents[TOP][Y] > paddleExtents[TOP][Y] and ballExtents[BOTTOM][Y] >= paddleExtents[TOP][Y] - 3) or \
               (ballExtents[BOTTOM][Y] < paddleExtents[BOTTOM][Y] and ballExtents[TOP][Y] <= paddleExtents[BOTTOM][Y] + 3)

    def Run(self) -> None:
        self.gameRunning = True
        while self.gameRunning == True:
            self.ProcessBallPosition()
            self.screen.update()
            time.sleep(0.001667)
        self.screen.bye()
