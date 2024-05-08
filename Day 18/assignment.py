import colorgram
from turtle import Turtle, Screen
import random

class HirstPaintingGenerator:
    
    def __init__(self, turtle:Turtle, screen:Screen) -> None:        
        self.turtle = turtle
        self.screen = screen
        self.screen.colormode(255)
        self.turtle.speed("fastest")
        self.rgbColors = list[tuple[int, int, int]]()
        #self.extactAndFillColors()
        self.rgbColors = [(207, 127, 127), (164, 38, 38), (140, 106, 106), (244, 57, 57), \
                          (3, 60, 60), (241, 140, 140), (249, 224, 224), (2, 185, 185), \
                          (162, 52, 52), (243, 162, 162), (53, 226, 226), (211, 234, 234), \
                          (251, 16, 16), (22, 128, 128), (220, 231, 231), (253, 253, 124), \
                          (27, 219, 219), (156, 168, 168), (236, 192, 192), (107, 102, 102), \
                          (142, 224, 224), (243, 151, 151), (160, 180, 180), (6, 36, 36)]

    #use if you have a new image you want to play with
    def extactAndFillColors(self):
        colors = colorgram.extract('image.jpg', 50)
        #skip the first two; they're just the white background and the canvas
        for color in colors:
            self.rgbColors.append((color.rgb.r, color.rgb.b, color.rgb.b))

    def Run(self, circleRadius:int, rows:int, columns:int, spacing:int) -> None:
        #start from the bottom left
        #one cirlce's radius from the bottom corner
        startingPosition = (-self.screen.window_width() / 2 + 2*circleRadius, -self.screen.window_height() / 2 + 2*circleRadius)
        self.turtle.teleport(startingPosition[0], startingPosition[1])
        self.turtle.hideturtle()
        for _ in range(rows):
            rowPosition = self.turtle.pos()
            for _ in range(columns):
                self.turtle.color(random.choice(self.rgbColors))
                #this was harder
                #self.turtle.begin_fill()
                #self.turtle.circle(circleRadius)
                #self.turtle.end_fill()
                self.turtle.dot(circleRadius)

                position = self.turtle.pos()
                self.turtle.teleport(position[0] + spacing + circleRadius, position[1])
            
            self.turtle.teleport(rowPosition[0], rowPosition[1] + spacing + circleRadius)
        



