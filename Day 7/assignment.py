import random
from hangman_art import *
from hangman_words import *

class HangmanGame:

    def __init__(self):
        #choose a random item in the list
        self.gameState = GameState()

    def _InitGame(self):    
        self.gameState = GameState(random.choice(word_list))
        print(logo)

    def _HandleGuess(self):
        guess = input("Guess a letter: ").lower()
        #checks whether the list has the item IN it
        while guess in self.gameState.Guesses:
            print(f"You've already guessed {guess}")
            guess = input("Guess a letter: ").lower()
        self.gameState.Guesses.append(guess)
        return guess

    def _EvaluateGuess(self, guess):
        # is the guessed letter in the target word
        if guess in self.gameState.TargetWord:
            #replace the '_' in the game board with the guessed letter
            for i in range(len(self.gameState.TargetWord)):
                if self.gameState.TargetWord[i] == guess:
                    self.gameState.GameBoard[i] = guess
        # not in the target word, lose a life
        else:
            self.gameState.Lives -= 1

        if "_" not in self.gameState.GameBoard or self.gameState.Lives == 0:
            self.gameState.GameOver = True

    def _PrintGameBoard(self):
        output = []
        for c in self.gameState.GameBoard:
            output += c
            output += " "
        print(stages[self.gameState.Lives])
        print("".join(output))

    def Game(self):
        self._InitGame()
        while (not self.gameState.GameOver):
            self._PrintGameBoard()
            guess = self._HandleGuess()
            self._EvaluateGuess(guess)
            
        if self.gameState.Lives > 0:
            print("You Win!")
        else:
            print(stages[0])
            print("You lose.")
        print("Game Over")

#here we're going to make use of properties
#ok, no we're not
#they're commented out now

class GameState:
    def __init__(self, targetWord = ""):
        self.TargetWord = targetWord
        self.Guesses = []
        self.GameOver = False
        self.MaxLives = 6
        self.Lives = self.MaxLives
        self.GameBoard = []
        self._SetupGameBoard()
    
    def _SetupGameBoard(self):
        for i in range(len(self.TargetWord)):
            self.GameBoard.append("_")

    # def getTargetWord(self):
        # return self.TargetWord
    # def setTargetWord(self,value:str):
        # self.TargetWord = value
        # for i in range(len(value)):
            # self.GameBoard += "_"
    # def deleteTargetWord(self):
        # del self.TargetWord
    
    # def getGuesses(self):
        # return self.Guesses
    # def setGuesses(self,value:list):
        # self.Guesses = value
    # def deletedGuesses(self):
        # del self.Guesses

    # def getGameOver(self):
        # return self.GameOver
    # def setGameOver(self,value):
        # self.GameOver = value
    # def deleteGameOver(self):
        # del self.GameOver

    # def getGameBoard(self):
        # return self.GameBoard
    # def setGameBoard(self,value):
        # self.GameBoard = value
    # def deleteGameBoard(self):
        # del self.GameBoard

    # def getLives(self):
        # return self.Lives
    # def setLives(self, value):
        # self.Lives = value
    # def deleteLives(self):
        # del self.Lives

    # TargetWord = property(getTargetWord, setTargetWord, deleteTargetWord)
    # Guesses = property(getGuesses, setGuesses, deletedGuesses)
    # GameOver = property(getGameOver, setGameOver, deleteGameOver)
    # GameBoard = property(getGameBoard, setGameBoard, deleteGameBoard)
    # Lives = property(getLives, setLives, deleteLives)