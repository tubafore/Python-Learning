class ConsoleParser:
    _invalidAnswer = "Not a valid answer"

    def acceptInput(message: str, validChoices: list, matchCase: bool = False) -> str:
        answer = input(message)
        if not matchCase:
            answer = answer.lower()

        while answer not in validChoices:
            print(ConsoleParser._invalidAnswer)
            answer = input(message)
            if not matchCase:
                answer = answer.lower()

        return answer


class CoffeeMachine:
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    money = {
        "penny": {"shortCode": "p", "value": 0.01},
        "nickle": {"shortCode": "n", "value": 0.05},
        "dime": {"shortCode": "d", "value": 0.1},
        "quarter": {"shortCode": "q", "value": 0.25}
    }

    def __init__(self):
        self.resources = CoffeeMachine.resources
        self.totalEarned = 0.0
        self.running = True
        self.menuOptions = []

        for option in CoffeeMachine.MENU:
            self.menuOptions.append(option)
        self.menuOptions.extend(['report', 'refill'])
        self.moneyOptions = []

        for option in CoffeeMachine.money:
            self.moneyOptions.append(option)
            self.moneyOptions.append(CoffeeMachine.money[option]["shortCode"])

        self.moneyOptions.append("refund")
        self.moneyOptions.append("r")

        menuMessages = [
            "What would you like? (",
            "/".join(CoffeeMachine.MENU),
            "): "
        ]

        self.menuMessage = "".join(menuMessages)

        moneyMessages = [
            "Please insert coins. (",
            "/".join(CoffeeMachine.money),
            "/refund"
            "): "
        ]

        self.moneyMessage = "".join(moneyMessages)

    def run(self):
        while self.running:
            menuChoice = ConsoleParser.acceptInput(self.menuMessage, self.menuOptions)
            if menuChoice == "report":
                self._displayReport()
            elif menuChoice == "refill":
                self._refill()
            else:
                self._handleDrinkChoice(menuChoice)

    def _displayReport(self):
        print(f"Water: {self.resources["water"]}ml")
        print(f"Milk: {self.resources["milk"]}ml")
        print(f"Coffee: {self.resources["coffee"]}g")
        print(f"Money: ${"{0:.2f}".format(self.totalEarned)}")

    def _refill(self):
        print("Restoring water, milk, and coffee")
        self.resources["water"] = 300
        self.resources["milk"] = 200
        self.resources["coffee"] = 100

    def _handleDrinkChoice(self, menuChoice:str):
        """
        Given a valid menuChoice, accept payment if resources are available
        and deduct resources, otherwise report resources unavailable
        :type menuChoice: str
        """
        choice = CoffeeMachine.MENU[menuChoice]
        if self._hasResources(choice):
            inserted = 0.0
            cost = choice["cost"]
            print(f"{menuChoice.title()} costs ${"{0:.2f}".format(cost)}")
            while inserted < cost:
                if inserted != 0.0:
                    print(f"Inserted ${"{0:.2f}".format(inserted)}")
                coin = ConsoleParser.acceptInput(self.moneyMessage, self.moneyOptions)
                if coin == "r" or coin == "refund":
                    print(f"${"{0:.2f}".format(inserted)} refunded")
                    inserted = 0.0
                    break
                elif coin == "p" or coin == "penny":
                    inserted += self.money["penny"]["value"]
                elif coin == "n" or coin == "nickle":
                    inserted += self.money["nickle"]["value"]
                elif coin == "d" or coin == "dime":
                    inserted += self.money["dime"]["value"]
                else:
                    inserted += self.money["quarter"]["value"]
            if inserted >= cost:
                #deduct the resources
                for ingredient in choice["ingredients"]:
                    self.resources[ingredient] -= choice["ingredients"][ingredient]
                #add the total
                self.totalEarned += cost
                #give the change if there is any
                if inserted > cost:
                    print(f"Here is your ${"{0:.2f}".format(inserted - cost)} in change.")
                #give them their drink
                print(f"Here is your {menuChoice} ☕ Emjoy!")

    def _hasResources(self, choice:dict) -> bool:
        result = True
        for ingredient in choice["ingredients"]:
            hasThis = self.resources[ingredient] >= choice["ingredients"][ingredient]
            result &= hasThis
            if not hasThis:
                print(f"Sorry, there is not enough {ingredient}")
        return result
