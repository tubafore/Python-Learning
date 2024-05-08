import art

class SilentAuction:
    def __init__(self):
        self.participants = {}

    def startAuction(self):
        print(art.logo)
        print("Welcome to the secret auction program.")
        self.acceptBid()

    def acceptBid(self):
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        self.participants[name] = bid
        self.continueAuction()

    def continueAuction(self):
        answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        while answer != 'yes' and answer != 'no':
            print("Command not understood")
            answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        self.clearScreen()
        if answer == 'yes':
            self.acceptBid()
        else:
            self.declareWinner()

    #solution from https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    def clearScreen(self):
        print("\033[H\033[J", end="")

    def declareWinner(self):
        winner = {
            "bid" : -999999, 
            "name": []
        }
        for key in self.participants:
            if self.participants[key] > winner["bid"]:
                winner["bid"] = self.participants[key]
                winner["name"] = [key]
            elif self.participants[key] == winner["bid"]:
                winner["name"].append(key)
        if (len(winner["name"]) < 2):
            print(f"The winner of the auction is {winner["name"]} with a bid of ${winner["bid"]}")
        else:
            print(f"We have a tie with {winner["name"]} with bids of ${winner["bid"]}")

        

