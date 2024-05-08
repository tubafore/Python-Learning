#a function with some datatype info in it
from assignment import TipCalculator

def aFunction():
    #Basic Data Types

    #Strings
    #the [] index the characters, 0-based
    print("Hello"[4])

    #Integer
    print(123 + 345)
    #replace commas with _ to make big numbers easier to read
    print(123_456_789)

    #Float
    print(3.14159)

    #Boolean
    #always capitalized
    print(True)

    #What type is this?
    print(type(len("Hello")))

    #Convert to string
    print("Your name has " + str(len("Jonathan")) + " characters in it")

def addDigits():
    two_digit_number = input()
    # 🚨 Don't change the code above 👆
    ####################################
    # Write your code below this line 👇
    number = int(two_digit_number)
    result = int(0)
    while (number > 0):
        #result += number % 10
        #number = int(number / 10)
        number, remainder = divmod(number, 10)
        result += remainder

    print(result)

#Math info
    
def mathInfo():
    print(3 + 5) #addition
    print(7 - 4) #subtraction
    print(3 * 2) #multiplication
    print(f"6 / 2 is {6/2} and always a {type(6/2)}") #division
    print(2 ** 3) #exponent 2 to the 3 power
    print(6 % 4) #mod
    print(8 ^ 9) #xor

def bmi():
    height = input("Enter height in meters e.g: 1.65\n")
    weight = input("Enter weight in kilograms e.g: 72\n")
    print(f"Your bmi is {int(float(weight)/(float(height) ** 2))}")

#more math functions
    
def moreMath():
    print(8/3)  #float
    print(8//3) #int rounded down
    print(-8//3) #int rounded down
    print(int(8/3)) #regular int conversion
    print(f"{round(8/3)} is type {type(round(8/3))}") #int
    print(f"{round(8/3, 2)} is type {type(round(8/3, 2))}") #float

#optional parameter
def lifeInWeeks(ageAtDeath = 90):
    age = input("Enter your age in years\n")
    print(f"You have {(ageAtDeath - int(age))*52} weeks left.")

calculator = TipCalculator()
calculator.CalculateTip()