from turtle import Turtle, Screen
import time
import pandas

class StatesGame:
    def __init__(self) -> None:
        self.States = pandas.read_csv("50_states.csv")
        self.Screen = Screen()
        self.Turtle = Turtle()
        self.Writer = Turtle()
        self.Writer.penup()
        self.Writer.hideturtle()
        self.Turtle.penup()
        self.setupScreen()
        self.gameRunning = False
        self.statesGuessed = list[str]()

    def setupScreen(self) -> None:
        self.Screen.setup(height=491, width=725)
        self.Screen.title("US States Game")
        self.Screen.addshape("map.gif")
        self.Turtle.shape("map.gif")
        self.Screen.listen()
        self.Screen.onkeyrelease(self.Quit, "Escape")

    def Quit(self) -> None:
        self.gameRunning = False
        self.Screen.bye()

    def AcceptGuess(self) -> str:
        title = "Guess a state"
        if len(self.statesGuessed) > 0:
            title = f"{len(self.statesGuessed)}/50 correct"
        guess = self.Screen.textinput(title=title, prompt="What's another state's name?")
        if guess is not None:
            #to capitalize each word, use .title()
            return f'{guess.title()}'
        return ""
    
    def HandleGuess(self, guess:str) -> None:
        if guess in self.statesGuessed or guess == "":
            return
        if guess in self.States["state"].array:
            self.statesGuessed.append(guess)
            self.WriteState(guess)

    def WriteState(self, guess:str) -> None:
        #this gets the row where the value in the "state" column equals the guess
        state = self.States[self.States["state"] == guess]
        self.Writer.teleport(state['x'].item(), state['y'].item())
        self.Writer.write(guess)

    def SaveMissingStates(self) -> None:
        if len(self.statesGuessed) == 50:
            return
        # result = list[str]()
        # for state in self.States["state"]:
        #     if state not in self.statesGuessed:
        #         result.append(state)
        # the above using list comprehension
        result = [state for state in self.States["state"] if state not in self.statesGuessed]
        converted = pandas.DataFrame(result)
        converted.to_csv("states_to_learn.csv")
        self.gameRunning = False
        self.Screen.bye()
        
    
    def Play(self) -> None:
        self.gameRunning = True
        while self.gameRunning and len(self.statesGuessed) < 50:
            guess = self.AcceptGuess()
            while guess == None:
                guess = self.AcceptGuess()
            if guess != "Exit":
                self.HandleGuess(guess)
            else:
                self.SaveMissingStates()