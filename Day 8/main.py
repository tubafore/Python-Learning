import math
from assignment import CaesarCipher

#more function notes
def greet_with(name:str, location:str):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#you can call a function with named parameters if you'd like
#if you do, parameter order does not matter
#greet_with(location="home", name="Jonathan")

def paint_calc(height:int, width:int, cover:int):
    return int(math.ceil((height * width)/cover))

def prime_checker(number:int):
    stop = int(math.ceil(math.sqrt(number)))
    prime = True
    for i in range(2, stop):
        if prime and number % i == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
cipher = CaesarCipher()
cipher.acceptInstruction()