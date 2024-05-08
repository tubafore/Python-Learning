#using decimal to get fixed point support
#the quantize method converts to a specified format

from decimal import *


class TipCalculator:
    def __init__(self):
        self.totalBill = 0
        self.tipPercentage = 0
        self.partySize = 0;
    
    def CalculateTip(self):
        print("welcome to the tip calculator.")
        self.totalBill = float(input("What was the total bill? $"))
        self.tipPercentage = int(input("How much tip would you like to give?  10, 12, or 15? "))
        self.partySize = int(input("How many people to split the bill? "))
        
        # Using a format string
        finalAmount = "{:.2f}".format((self.totalBill * (1 + (self.tipPercentage / 100)) / self.partySize))
        print(f"Each person should pay: ${ finalAmount }")

        # The quantize(Decimal(str)) method uses the argument to specify the format for converting
        # the calling decimal's value to a string.
        # this gives us exactly 2 points of precision
        print(f"Each person should pay: ${Decimal(self.totalBill * (1 + (self.tipPercentage / 100)) / self.partySize).quantize(Decimal("1.00")) }")