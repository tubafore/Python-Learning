#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import *
import random

class ConsoleParser:
    _invalidAnswer = "Not a valid answer"
    def AcceptInput(message:str, validChoices:list, matchCase:bool = False) -> str:
        answer = input(message)
        if matchCase == False:
            answer = answer.lower()
        
        while answer not in validChoices:
            print(ConsoleParser._invalidAnswer)
            answer = input(message)
            if matchCase == False:
                answer = answer.lower()
        
        return answer

class GuessingGame:
    #it really is just like json
    _gameLevels = { 
        "easy" : 10, 
        "hard" : 5
    }
    _tooHigh = "Too High."
    _tooLow = "Too Low."
    _teaser = "I'm thinking of a number between 1 and 100."
    _difficultyMessage = "Choose a difficulty. Type 'easy' or 'hard': "
    _guessRequest = "Make a guess: "
    _remaining = "You have {remainingGuesses} attempts remaining to guess the number."
    _again = "Guess again."
    _win = "You Win!"
    _lose = "You Lose."

    def __init__(self):
        self.remainingGuesses = 10
        self.targetNumber = 0
        self.gameOver = False

    def Play(self):
        print(logo)
        print(GuessingGame._teaser)
        easyHard = ConsoleParser.AcceptInput(GuessingGame._difficultyMessage, GuessingGame._gameLevels)
        self.remainingGuesses = GuessingGame._gameLevels[easyHard]
        self.targetNumber = random.randint(1, 100)
        while self.remainingGuesses > 0 and self.gameOver == False:
            print(GuessingGame._remaining.format(remainingGuesses = self.remainingGuesses))
            guess = int(input(GuessingGame._guessRequest))
            if guess != self.targetNumber:
                self.remainingGuesses -= 1
                if guess > self.targetNumber:
                    print(GuessingGame._tooHigh)
                else:
                    print(GuessingGame._tooLow)
                if self.remainingGuesses == 0:
                    print(GuessingGame._lose)
                    self.gameOver = True
            else:
                print(GuessingGame._win)
                self.gameOver = True

            
            

