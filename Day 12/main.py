from assignment import *

#scope notes

#global scope

somethingDefinedOutsideEverything = "like this"

def anotherGlobalFunction():
    def butThisIsValid():
        print ("And just wrong in my opinion")
    
    #can only be called from within this function
    butThisIsValid()
    #this is creating a new, locally-scoped variable with the same name as the globally scoped variable
    somethingDefinedOutsideEverything = "not like this"
    print(somethingDefinedOutsideEverything)
    #this will revert to its previous value after running the function

# print(somethingDefinedOutsideEverything)
# anotherGlobalFunction()
# print(somethingDefinedOutsideEverything)

# there is no block level scoping (like within for loops, if statements, etc.)
    
def blockLevelScopingExample():
    game_level = 3
    enemies = ["skeleton", "zombie", "alien"]
    if (game_level < 5):
        #notice the variable is created within an if statement
        #this is different from C# behavior
        new_enemy = enemies[0]
    print(new_enemy)

# blockLevelScopingExample()

# functions create a scope

# modifying globally scoped variables
# generally you're not gonna do this
def modifyingGloballyScopedVariables():
    # used only if we're going to modify it
    # you can still use its value without the global keyword
    global somethingDefinedOutsideEverything
    print(f"changing somethingDefinedOutsideEverything from '{somethingDefinedOutsideEverything}'")
    somethingDefinedOutsideEverything = "not like this"

# modifyingGloballyScopedVariables()
# print(f"somethingDefinedOutsideEverything is now '{somethingDefinedOutsideEverything}'")
    
# here we access the global variable's value without using the global keyword
def properlyModifyingGloballyScopedVariables():
    return somethingDefinedOutsideEverything + " is also wrong but somehow works"

# print(somethingDefinedOutsideEverything)
# somethingDefinedOutsideEverything = properlyModifyingGloballyScopedVariables()
# print(somethingDefinedOutsideEverything)

#if you need a global constant, name it in ALLCAPS

game = GuessingGame()
game.Play()