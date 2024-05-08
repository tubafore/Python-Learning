from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Draw(0,0)
        
    def Draw(self, player1Score:int, player2Score:int) -> None:
        self.clear()
        self.teleport(-100, 200)
        self.write(player1Score, align="center", font=("Consolas", 80, "bold"))
        self.teleport(100, 200)
        self.write(player2Score, align="center", font=("Consolas", 80, "bold"))
        