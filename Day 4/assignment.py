import random

class PaperRockScissorsGame:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def PrintChoice(choice:int):
        if choice == PaperRockScissorsGame.PAPER:
            print(PaperRockScissorsGame.paper)
        elif choice == PaperRockScissorsGame.ROCK:
            print(PaperRockScissorsGame.rock)
        elif choice == PaperRockScissorsGame.SCISSORS:
            print(PaperRockScissorsGame.scissors)

    def DetermineWinner(userChoice, computerChoice):
        if userChoice == computerChoice:
            print("It's a draw")
            return
        #using the parentheses allows the multiline if statement
        if (userChoice == PaperRockScissorsGame.ROCK and computerChoice == PaperRockScissorsGame.SCISSORS or
            userChoice == PaperRockScissorsGame.SCISSORS and computerChoice == PaperRockScissorsGame.PAPER or
            userChoice == PaperRockScissorsGame.PAPER and computerChoice == PaperRockScissorsGame.ROCK):
            print("You win!")
        #using the \ allows this version of the multiline if statement
        #if userChoice == PaperRockScissorsGame.ROCK and computerChoice == PaperRockScissorsGame.SCISSORS or \
        #   userChoice == PaperRockScissorsGame.SCISSORS and computerChoice == PaperRockScissorsGame.PAPER or \
        #   userChoice == PaperRockScissorsGame.PAPER and computerChoice == PaperRockScissorsGame.ROCK:
        #    print("You win!")
        else:
            print("You lose.")

    def Game():
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
        computerChoice = random.randint(0,2)
        PaperRockScissorsGame.PrintChoice(choice)
        print("Computer Chose:")
        PaperRockScissorsGame.PrintChoice(computerChoice)
        PaperRockScissorsGame.DetermineWinner(choice, computerChoice)
        potentialYes = input("Type yes or y to play again\n").lower()
        if (potentialYes == 'y' or potentialYes == "yes"):
            PaperRockScissorsGame.Game()

        
