from art import *
import re

class CaesarCipher:
    #get all the letters using chr (character from int) and ord (int from character)
    #for i in range(0,26):
    #   print(chr(i + ord('a')))
    letters = ['a','b','c','d','e','f','g','h','i','j', \
               'k','l','m','n','o','p','q','r','s','t', \
               'u','v','w','x','y','z']
    
    def __init__(self):
        print(logo)

    def encode(message:str,shift:int):
        output = []
        for char in message:
            output.append(CaesarCipher.letters[(CaesarCipher.letters.index(char) + shift) % 26])
        print(f"The encoded text is {"".join(output)}")

    def decode(message:str,shift:int):
        output = []
        for char in message:
            output.append(CaesarCipher.letters[(CaesarCipher.letters.index(char) - shift) % 26])
        print(f"The encoded text is {"".join(output)}")
    
    def fullCipher(message:str,shift:int,encode:bool):
        output = []
        #encoding is shifting to the right (incrementing), decoding is to the left (decrementing)
        if not encode:
            shift = -shift
        for char in message:
            #use a regular expression for fun
            #if re.match("[a-z]", char):
            if char in CaesarCipher.letters:
                output.append(CaesarCipher.letters[(CaesarCipher.letters.index(char) + shift) % 26])
            else:
                output.append(char)
        print(f"The encoded text is {"".join(output)}")
        

    #can be eliminated
    #creating slices
    def rotate(count:int):
        #get characters from count to the end
        result = CaesarCipher.letters[count:]
        #get characters from beginning to the count
        result.extend(CaesarCipher.letters[0:count])
        return result
    
    def acceptInstruction(self):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        while direction != 'encode' and direction != 'decode':
            print("Command not understood")
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        CaesarCipher.fullCipher(text, shift, direction == 'encode')
        
        yes = input("Type 'yes' if you want to go again.  Otherwise type 'no'\n").lower()
        while yes != 'yes' and yes != 'no':
            print("Command not understood")
            yes = input("Type 'yes' if you want to go again.  Otherwise type 'no'\n").lower()
        
        if yes == "yes":
            CaesarCipher.acceptInstruction(self)
        else:
            print("Goodbye")

        
        

