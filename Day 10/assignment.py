import re
from art import logo

class TextCalculator:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.validOperations = {
            '+': TextCalculator.add,
            '-': TextCalculator.subtract,
            '*': TextCalculator.multiply,
            '/': TextCalculator.divide
        }
        self.operationsValidator = "[\+\-\*/]"
        self.currentTotal = 0
    
    def add(a:float, b:float) -> float:
        return a + b
    def subtract(a:float, b:float) -> float:
        return a - b
    def multiply(a:float, b:float) -> float:
        return a * b
    def divide(a:float, b:float) -> float:
        return a / b

    def Run(self):
        print(logo)
        self.DoCalculation()

    def DoCalculation(self, keepGoing:bool = False):
        if not keepGoing:
            self.number1 = float(input("What's the first number?: "))

        for operator in self.validOperations:
            print(operator)
        chosenOperator = input("Pick an operation: ")
        while not re.match(self.operationsValidator, chosenOperator):
            print("Not a valid operator, please see above")    
            chosenOperator = input("Pick an operation: ")
        self.number2 = float(input("What's the next number?: "))
        self.currentTotal = self.validOperations[chosenOperator](self.number1, self.number2)
        print(f"{self.number1} {chosenOperator} {self.number2} = {self.currentTotal}")
        keepGoing = input(f"Type 'y' to continue calculating with {self.currentTotal}, or type 'n' to start a new calculation: ").lower()
        while keepGoing != 'y' and keepGoing != 'n':
            print("Invalid choice")
            keepGoing = input(f"Type 'y' to continue calculating with {self.currentTotal}, or type 'n' to start a new calculation: ").lower()
        
        if keepGoing == 'y':
            self.number1 = self.currentTotal
            self.DoCalculation(True)
        else:
            self.Run()    

    #This was making it too hard
    # def DoCalculation(self, keepGoing:bool = False):
    #     if not keepGoing:
    #         self.number1 = float(input("What's the first number?: "))

    #     for operator in self.validOperations:
    #         print(operator)
    #     chosenOperator = input("Pick an operation: ")
    #     while not re.match(self.operationsValidator, chosenOperator):
    #         print("Not a valid operator, please see above")    
    #         chosenOperator = input("Pick an operation: ")
    #     operator = MathOperatorParser.Parse(chosenOperator)
    #     self.number2 = float(input("What's the next number?: "))
    #     self.currentTotal = operator.Perform(self.number1, self.number2)
    #     print(f"{self.number1} {chosenOperator} {self.number2} = {self.currentTotal}")
    #     keepGoing = input(f"Type 'y' to continue calculating with {self.currentTotal}, or type 'n' to start a new calculation: ").lower()
    #     while keepGoing != 'y' and keepGoing != 'n':
    #         print("Invalid choice")
    #         keepGoing = input(f"Type 'y' to continue calculating with {self.currentTotal}, or type 'n' to start a new calculation: ").lower()
        
    #     if keepGoing == 'y':
    #         self.number1 = self.currentTotal
    #         self.DoCalculation(True)
    #     else:
    #         self.DoCalculation()    


# this was making it too hard because I didn't know you could put a function in a dictionary
class MathOperator:
    # the -> shows the return type
    # the """ string """ as the first line of the function is the docstring and shows up
    # on hover
    def Perform(number1:float, number2:float) -> float:
        """Do the operation: number1 OPERATOR number2 and return the result"""
        pass

class AdditionOperator(MathOperator):
    def Perform(number1: float, number2: float) -> float:
        return number1 + number2
    
class SubtractionOperator(MathOperator):
    def Perform(number1: float, number2: float) -> float:
        return number1 - number2

class MultiplicationOperator(MathOperator):
    def Perform(number1: float, number2: float) -> float:
        return number1 * number2

class DivisionOperator(MathOperator):
    def Perform(number1: float, number2: float) -> float:
        return number1 / number2

#class declaration order matters in python
#that's why this is at the bottom    
class MathOperatorParser:
    def Parse(input:str) -> MathOperator:
        if input == '+':
            return AdditionOperator
        elif input == '-':
            return SubtractionOperator
        elif input == "*":
            return MultiplicationOperator
        else:
            return DivisionOperator
