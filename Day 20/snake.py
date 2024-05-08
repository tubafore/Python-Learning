from turtle import Turtle

class Snake:
    def __init__(self) -> None:
        #reminder, if you want to specify the type, put those parentheses in 
        self.Body = list[Turtle]()
        self.SnakeSize = 20
        for _ in range(3):
            self._addBodySegment()
    
    def Head(self) -> Turtle:
        return self.Body[0]

    def _addBodySegment(self) -> None:
        heading = 0
        position = (0,0)
        if len(self.Body) > 0:
            heading = self.Body[-1].heading()
            position = self.Body[-1].position()
        newTurtle = self._createBodySegment()
        newTurtle.setheading(heading)
        newTurtle.setposition(position)
        newTurtle.backward(self.SnakeSize)
        self.Body.append(newTurtle)

    def _createBodySegment(self) -> Turtle:
        result = Turtle("square")
        result.color("white")
        result.penup()
        result.speed("fastest")
        return result

    
    def Move(self, distance:float = 20) -> None:
        for i in range(len(self.Body) - 1, 0, -1):
            if i > 0:
                self.Body[i].setposition(self.Body[i-1].position())
                self.Body[i].setheading(self.Body[i-1].heading())
        self.Head().forward(distance)