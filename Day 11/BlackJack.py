from art import *
import random

class Card:
    def __init__(self, type:str, suit:str):
        self.type = CardTypes[type]
        self.suit = suit


class Deck:
    def __init__(self):
        self.Cards = []
        self.Fill()

    def Fill(self):
        self.Cards.clear()
        for suit in Suits:
            for cardType in CardTypes:
                self.Cards.append(Card(cardType, suit))
    
    def Shuffle(self):
        random.shuffle(self.Cards)
    
    
class Hand:
    def __init__(self):
        self.Cards = []
    
    def getScore(self) -> int:
        scores = []
        for card in self.Cards:
            scores.append(card.type["value"])
        
        while sum(scores) > 21 and 11 in scores:
            scores[scores.index(11)] = 1

        return sum(scores)

    

class BlackJack:
    def __init__(self):
        self.PlayerHand = Hand()
        self.DealerHand = Hand()
        self.Deck = Deck()
        self._resetGame()

    def _resetGame(self):
        self.PlayerHand.Cards.clear()
        self.DealerHand.Cards.clear()
        self.Deck.Fill()
        self.Deck.Shuffle()

    def _dealCard(self, hand:Hand):
        hand.Cards.append(self.Deck.Cards.pop(0))

    def ClearTerminal() :
        print("\033[H\033[J", end="")

    def _printGameBoard(self,showDealerCard:bool = False):
        BlackJack.ClearTerminal()
        print(logo)
        print("Your hand")
        BlackJack._printHand(self.PlayerHand)
        print("Dealer hand")
        BlackJack._printHand(self.DealerHand, showDealerCard)

    def _printHand(hand:Hand, showSecondCard:bool = True):
        for i in range(0, 9):
            line = []
            for card in range(len(hand.Cards)):
                renderString = hand.Cards[card].type["renderStrings"][i]
                if card == 1 and showSecondCard == False:
                    renderString = EmptyCard["renderStrings"][i]
                
                if renderString == TopValueLine or renderString == BottomValueLine:
                    line.append(renderString.format(shortString = hand.Cards[card].type["shortString"]))
                elif renderString == SingleSuitLine or renderString == DoubleSuitLine:
                    line.append(renderString.format(suit = Suits[hand.Cards[card].suit]))
                else:
                    line.append(renderString)
            print("".join(line))

    def _startGame(self):
        self._dealCard(self.PlayerHand)
        self._dealCard(self.DealerHand)
        self._dealCard(self.PlayerHand)
        self._dealCard(self.DealerHand)

    def Play(self):
        self._startGame()
        keepDealing = True
        while keepDealing == True:
            self._printGameBoard()

            if self.PlayerHand.getScore() > 21:
                keepDealing = False

            if keepDealing == True:
                answer = BlackJack.AcceptYesNo("Type 'y' to get another card, type 'n' to pass: ")
                if answer == 'y':
                    self._dealCard(self.PlayerHand)
                else:
                    keepDealing = False
            
        while self.DealerHand.getScore() <= 16:
            self._dealCard(self.DealerHand)

        self._printGameBoard(showDealerCard=True)
        dealerScore = self.DealerHand.getScore()
        playerScore = self.PlayerHand.getScore()

        if (dealerScore > 21 and playerScore <= 21) or (playerScore > dealerScore and playerScore <= 21):
            print("You Win.")
        elif (playerScore < dealerScore) or (playerScore > 21):
            print("You lose.")
        else:
            print("Tie")

        answer = BlackJack.AcceptYesNo("Do you want to play another game of Blackjack?  Type 'y' or 'n': ")
        if answer == 'y':
            self._resetGame()
            self.Play()

    def AcceptYesNo(message:str) -> str:
        answer = input(message)

        while answer != "y" and answer != "n":
            print("Command not understood")
            answer = input(message)
        
        return answer





