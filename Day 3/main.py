from assignment import Game

# If/else statements
def RollercoasterHeightCheck(heightInCm:int):
    if heightInCm >= 120 or heightInCm == 69:
    #if (heightInCm >= 120)   #can have parentheses or not
        print("You can ride the rollercoaster")
        return True
    else:
        print("Sorry, you have to grow taller before you can ride")
        return False


def IsEven(number:int):
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

# Nested If/else statements
def RollercoasterHeightCheckWithShakedown(heightInCm:int):
    if RollercoasterHeightCheck(heightInCm):
    #if (heightInCm >= 120)   #can have parentheses or not
        total = 0
        age = int(input("What is your age?\n"))
        if age < 12:
            total = 5
        #else if statement    
        elif age > 18:
            if not age >= 45 and age <= 55:
                total = 12
            print("Everything is going to be ok.  Have a free ride on us!")
        else:
            total = 7

        wantPhotos = input("Want photos?\n")
        if wantPhotos.lower() == "yes":
            total += 3
        
        print(f"The total bill is ${total}")


def bmi():
    height = input("Enter height in meters e.g: 1.65\n")
    weight = input("Enter weight in kilograms e.g: 72\n")
    bmi = float(weight)/(float(height) ** 2)
    interpretation = interpretBmi(bmi)
    bmiStr = "{:.1f}".format(bmi)
    print(f"Your BMI is {bmiStr}, {interpretation}")
    return bmi

def interpretBmi(bmi:float):
    if bmi < 18.5:
        return "you are underweight."
    elif bmi < 25:
        return "you have a normal weight."
    elif bmi < 30:
        return "you are slightly overweight."
    elif bmi < 35:
        return "you are obese."
    else:
        return "you are clinically obese."
    
def isLeapYear(year:int):
    if year % 400 == 0:
        print("Leap year")
    elif year % 4 == 0:
        if year % 100 == 0:
            print ("Not leap year")
        else:
            print("Leap year")
    else:
        print ("Not leap year")

# Ternary Operator!  Looks weird
def ToBool(arg:str):
    return True if arg.lower == "Y" else False

def pizzaCustomization(size:str, pepperoni:bool, extraCheese:bool):
    total = 15

    if (size.lower() == 'm'):
        total = 20
    elif(size.lower() == "l"):
        total = 25

    if total == 15:
        if pepperoni:
            total += 2
    elif pepperoni:
        total += 3

    if extraCheese:
        total += 1

    print("Thank you for choosing Python Pizza Deliveries!\n")
    print(f"Your final bill is: ${total}")
    
#Logical Operators
def logicalOperatorsExample():
    print(f"A and B = {True and True}")
    print(f"A or B = {True or True}")
    print(f"NOT A and B = {not True and True}")

def loveCalculator(name1:str,name2:str):
        true = "true"
        love = "love"
        combinedName = name1.lower() + name2.lower()
        trueTotal = 0
        loveTotal = 0

        for c in true:
            trueTotal += combinedName.count(c)
        
        for c in love:
            loveTotal += combinedName.count(c)
        
        #combine them to make a 2 digit score
        result = trueTotal * 10 + loveTotal

        if result < 10 or result > 90:
            print(f"Your score is {result}, you go together like coke and mentos.")
        elif result >= 40 and result <= 50:
            print(f"Your score is {result}, you are alright together.")
        else:
            print(f"Your score is {result}.")    

game = Game()
game.Run()
