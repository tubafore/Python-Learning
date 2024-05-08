from turtle import Turtle

class DrawingHelper:
    def DrawRectange(turtle:Turtle, width:int, height:int) -> None:
        '''Draws a width x height rectangle using the turtle'''
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(height)
            turtle.left(90)
            turtle.forward(width)
            turtle.left(90)
        turtle.end_fill()
