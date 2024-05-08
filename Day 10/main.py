from assignment import TextCalculator

#functions with outputs notes
#the -> specifies the output type
#the number:int specifies the argument type
def square(number:int) -> float:
    return number * number

# convert a name to regular Title Case
def format_name(fName:str, lName:str) -> str:
    #the hard way, slice just the first letter, then slice the rest 
    #fName = fName[:1].capitalize() + fName[1:].lower()
    #lName = lName[:1].capitalize() + lName[1:].lower()
    return f"{fName.title()} {lName.title()}"

#print(format_name("joNAtHan", "bLACKWELL"))




calc = TextCalculator()
calc.Run()
