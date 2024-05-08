# #inheritance notes

# class Animal:
#     def __init__(self) -> None:
#         self.numEyes = 2

#     def breathe(self):
#         print("inhale, exhale")

# #note the class in parentheses, that's the super class
# class Fish(Animal):
#     def __init__(self) -> None:
#         #calling the constructor of the super class
#         super().__init__()

#     #overriding a method involves calling it the same thing
#     def breathe(self):
#         #but if you still want to call it, super().methodName()
#         super().breathe()
#         print("doing this underwater")

#     def swim(self):
#         print("moving in water")

# nemo = Fish()
# nemo.breathe()

from game import SnakeGame

game = SnakeGame()
game.Run()