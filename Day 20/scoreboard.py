from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.scoreString = "Score : {score}"
        self.gameOverString = "Game Over"
        self.color("white")
        self.sety(270)
    
    def ShowScore(self, score:int) -> None:
        self.clear()
        self.write(self.scoreString.format(score = score), font=("Consolas", 20, "bold"), align="center")
    
    def ShowGameOver(self) -> None:
        self.sety(0)
        self.write(self.gameOverString, font=("Consolas", 20, "bold"), align="center")

