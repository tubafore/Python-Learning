from art import *
from data import *
import random
import re

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
    
class HigherLowerGame:
    _compareA = "Compare A: {data}"
    _againstB = "Against B: {data}"
    _dataFormat = "{name}, {aAn} {description}, from {country}"
    _moreFollowers = "Who has more followers?  Type 'A' or 'B': "
    _rightMessage = "You're right! Current score: {score}"
    _wrongMessage = "Sorry, that's wrong. Final score: {score}"

    def __init__(self):
        self.dataIndices = []
        for i in range(len(data)):
            self.dataIndices.append(i)
        self._reset()
    
    def ClearTerminal() :
        print("\033[H\033[J", end="")

    def _reset(self):
        random.shuffle(self.dataIndices)
        self.ComparisonAIndex = self.dataIndices[0]
        self.ComparisonBIndex = self.dataIndices[1]
        self.currentIndex = 1
        self.gameOver = False
        self.statusMessage = ""
        self.score = 0
        self.playerChoice = ""
    
    def _printGameLine(line:str, data:dict):
        aAnString = 'a'
        if re.match("[aeiouAEIOU]", data["description"][0]):
            aAnString += "n"
        print(line.format(data = HigherLowerGame._dataFormat.format(name = data['name'], aAn = aAnString, description = data['description'], country = data['country'])))

    def _checkAnswer(self):
        #check if a is less than b to see if the game is over
        if self.playerChoice == 'a':
            self.gameOver = data[self.ComparisonAIndex]["follower_count"] < data[self.ComparisonBIndex]["follower_count"]
        #check if a is greater than b to see if the game is over
        else:
            self.gameOver = data[self.ComparisonAIndex]["follower_count"] > data[self.ComparisonBIndex]["follower_count"]

        if self.gameOver:
            self.statusMessage = HigherLowerGame._wrongMessage.format(score = self.score)
        else:
            self.score += 1
            self.currentIndex += 1
            # if they get all of them right, bravo!  game over
            self.gameOver = self.currentIndex >= len(data)
            self.statusMessage = HigherLowerGame._rightMessage.format(score = self.score)
            #copy the comparison from b if b is the correct answer
            if self.playerChoice == 'b':
                self.ComparisonAIndex = self.ComparisonBIndex
            #move on to the next person
            self.ComparisonBIndex = self.dataIndices[self.currentIndex]

    def Play(self):
        while not self.gameOver:
            HigherLowerGame.ClearTerminal()
            print(logo)
            if self.playerChoice != "":
                self._checkAnswer()
            if self.statusMessage != "":
                print(self.statusMessage)
            if not self.gameOver:
                HigherLowerGame._printGameLine(HigherLowerGame._compareA, data[self.ComparisonAIndex])
                print(vs)
                HigherLowerGame._printGameLine(HigherLowerGame._againstB, data[self.ComparisonBIndex])
                self.playerChoice = ConsoleParser.AcceptInput(HigherLowerGame._moreFollowers, ['a', 'b'])
            else:
                choice = ConsoleParser.AcceptInput("Play Again? Type 'Y' or 'N': ", ['y', 'n'])
                if choice == 'y':
                    self._reset()
                


