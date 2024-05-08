#import from other python files in the same directory
#.assignment (the name of the file)
#BandNameGenerator (the name of the class)
from assignment import BandNameGenerator

#variable declaration
five = 5

#string interpolation
print(f"""Hello World! {five}
       This is a multiline string...potentially
      """)

#reading input from the console, the string is the prompt.
#this always returns a string
name = input("What's your name? ")
print(f"'Sup {name}?")

#strings can start with single or double quotes like javascript
print('Righteous!')

#parse a string as an int
aNumber = int(input("Give me a number: "))
print(f"{aNumber}*5 = {aNumber*5}")

print("----------------------------------------------------------------------")
generator = BandNameGenerator()
print(f"Your band name could be {generator.DoTheThing()}")

