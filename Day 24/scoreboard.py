from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.scoreString = "Score : {score} High Score: {highScore}"
        self.gameOverString = "Game Over"
        self.color("white")
        self.sety(270)
    
    def ShowScore(self, score:int, highScore:int) -> None:
        self.clear()
        self.write(self.scoreString.format(score = score, highScore = highScore), font=("Consolas", 20, "bold"), align="center")
    
    def ShowGameOver(self) -> None:
        self.sety(0)
        self.write(self.gameOverString, font=("Consolas", 20, "bold"), align="center")

