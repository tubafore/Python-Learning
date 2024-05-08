from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.Velocity = tuple[float,float]
        self.Colliding = False

    def reflectVelocity(self, vertical:bool = False) -> None:
        if vertical:
            self.Velocity = (self.Velocity[0] * -1, self.Velocity[1])
        else:
            self.Velocity = (self.Velocity[0], self.Velocity[1] * -1)