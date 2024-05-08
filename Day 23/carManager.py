from turtle import _Screen
from car import Car
from player import Player
from constants import *
import random

class CarManager:
    def __init__(self, screen:_Screen) -> None:
        self.Cars = list[Car]()
        self.Speed = STARTING_MOVE_DISTANCE
        self.GenerationRate = CAR_GENERATION_FREQUENCY
        self.screenWidth = screen.window_width()
        self.screenHeight = screen.window_height()
        self.halfScreenWidth = self.screenWidth / 2
        self.halfScreenHeight = self.screenHeight / 2 - CAR_PADDING
        self.PotentiallyGenerateCar()

    def Reset(self) -> None:
        self.IncreaseSpeed()
        if self.GenerationRate > 1:
            self.GenerationRate -= 1

    def IncreaseSpeed(self) -> None:
        self.Speed += MOVE_INCREMENT

    def MoveCars(self) -> None:
        self.CullCars()
        self.PotentiallyGenerateCar()
        for car in self.Cars:
            car.forward(self.Speed)

    def CullCars(self) -> None:
        carsToRemove = []
        for car in self.Cars:
            if car.xcor() < -self.halfScreenWidth - 20:
                carsToRemove.append(car) 

        for car in carsToRemove:
            self.Cars.remove(car)

        for i in range(len(carsToRemove)-1,-1,-1):
            del carsToRemove[i]

    def PotentiallyGenerateCar(self) -> None:
        if random.randint(0,self.GenerationRate) == self.GenerationRate:
            newCar = Car()
            newCar.setposition(self.halfScreenWidth, random.randint(int(-self.halfScreenHeight + 10), int(self.halfScreenHeight - 10)))
            self.Cars.append(newCar)

    def CheckForCollisions(self, player:Player) -> bool:
        playerExtents = player.GetExtents()
        for car in self.Cars:
            carExtents = car.GetExtents()
            if CarManager.DoExtentsCollide(playerExtents, carExtents):
                return True
        return False

    def DoExtentsCollide(first:list[tuple[float, float]], second:list[tuple[float, float]]) -> bool:
        if len(first) != 2 or len(second) != 2:
            raise Exception("Each argument must contain exactly 2 tuples")
        if (second[TOP][X] <= first[TOP][X] and first[TOP][X] <= second[BOTTOM][X]) or \
           (second[TOP][X] <= first[BOTTOM][X] and first[BOTTOM][X] <= second[BOTTOM][X]):
            if (second[BOTTOM][Y] <= first[TOP][Y] and first[TOP][Y] <= second[TOP][Y]) or \
               (second[BOTTOM][Y] <= first[BOTTOM][Y] and first[BOTTOM][Y] <= second[TOP][Y]):
                return True
        return False