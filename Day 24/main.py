#working with files notes

#your basic read the contents of a file sequence, opening in read mode
# file = open("my file.txt")
# contents = file.read()
# print(contents)
# file.close()

# C# using block equivalent, opening in read mode
# with open("my file.txt") as file:
#     contents = file.read()
#     print(contents)

# Open a file in write mode and write contents to it
# this will create a new file if it doesn't exist
# with open("my file.txt", mode="w") as file:
#     file.write("New text.")

# # Open a file in APPEND mode and write contents to it
# with open("my file.txt", mode="a") as file:
#     file.write("New text.")

# opening the file in the same directory as the exe
# with open("my file.txt") as file:
#     contents = file.read()
#     print(contents)

# opening the file with the absolute path
# both work the same, note using the / version starts from the drive
# with open("C:\\Users\\Jonathan\\source\\repos\\Python\\Day 24\\data.txt") as file:
# with open("/Users/Jonathan/source/repos/Python/Day 24/data.txt") as file:
#     contents = file.read()
#     print(contents)

# opening the file with a relative path
# with open("../../../../desktop/this one.txt") as file:
#     contents = file.read()
#     print(contents)

# from game import SnakeGame

# game = SnakeGame()
# game.Run()

from assignment import LetterGenerator

gen = LetterGenerator()