import random

class PasswordGenerator:
    Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', \
               'W', 'X', 'Y', 'Z']
    Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    LETTER = 0
    NUMBER = 1
    SYMBOL = 2

    def GetRandomLetter():
        return PasswordGenerator.Letters[random.randint(0, len(PasswordGenerator.Letters)-1)]
        # better way
        # random.choice(PasswordGenerator.Letters)
    
    def GetRandomNumber():
        return PasswordGenerator.Numbers[random.randint(0, len(PasswordGenerator.Numbers)-1)]
        # better way
        # random.choice(PasswordGenerator.Numbers)
    
    def GetRandomSymbol():
        return PasswordGenerator.Symbols[random.randint(0, len(PasswordGenerator.Symbols)-1)]
        # better way
        # random.choice(PasswordGenerator.Symbols)
    
    def Generate():
        print("Welcome to the PyPassword Generator!")
        desiredLettersCount = int(input("How many letters would you like in your password?\n")) 
        desiredSymbolsCount = int(input(f"How many symbols would you like?\n"))
        desiredNumbersCount = int(input(f"How many numbers would you like?\n"))

        desiredTotal = desiredLettersCount + desiredSymbolsCount + desiredNumbersCount
        characters = []

        letterCount = 0
        symbolCount = 0
        numberCount = 0
        total = 0

        while total < desiredTotal:
            choice = random.randint(0, 2)
            if choice == PasswordGenerator.LETTER and letterCount < desiredLettersCount:
                characters.append(PasswordGenerator.GetRandomLetter())
                letterCount += 1
                total += 1
            elif choice == PasswordGenerator.NUMBER and numberCount < desiredNumbersCount:
                characters.append(PasswordGenerator.GetRandomNumber())
                numberCount += 1
                total += 1
            elif symbolCount < desiredSymbolsCount:
                characters.append(PasswordGenerator.GetRandomSymbol())
                symbolCount += 1
                total += 1
        # Seems to be the way to do faster string concatenation in python
        # rough equivalent of StringBuilder in c#
        print (''.join(characters))

        #easier way
        for i in range(0, desiredLettersCount):
            characters.append(random.choice(PasswordGenerator.Letters))
        for i in range(0, desiredNumbersCount):
            characters.append(random.choice(PasswordGenerator.Numbers))
        for i in range(0, desiredSymbolsCount):
            characters.append(random.choice(PasswordGenerator.Symbols))
        random.shuffle(characters)
        print(''.join(characters))