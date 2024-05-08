from tkinter import *
from constants import *

from states import States

class Pomodoro:
    DEBUG = False

    def __init__(self) -> None:
        self.completedPomodoros = 0
        self.endTimeInSeconds = -1
        self.window = Tk()
        self.canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
        self.timerCanvasText = -1
        self.photoImage = PhotoImage(file="tomato.png")
        self.timerStateLabel = Label(text="Timer", font=(FONT_NAME, 50, "bold"), foreground=GREEN, background=YELLOW)
        self.checkLabel = Label(fg=GREEN, background=YELLOW, font=(FONT_NAME, 30, "bold"))
        self.startButton = Button(text="Start", command=self.startClick)
        self.resetButton = Button(text="Reset", command=self.resetClick)
        self.timerCancellationHandle = ""
        self.state = States.NONE
        self.timerInterval = 1000
        if Pomodoro.DEBUG:
            self.timerInterval = 10
        self.setupUI()
        self.window.mainloop()

    def setupUI(self) -> None:
        self.window.title("Pomodoro")
        self.window.configure(padx=100, pady=50, bg=YELLOW)
        #specify the location of the center of the image for some reason
        self.canvas.create_image(100, 110.5, image=self.photoImage)
        self.timerCanvasText = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.timerStateLabel.grid(row=0, column=1)
        self.canvas.grid(row=1, column=1)
        self.startButton.grid(row=2, column=0)
        self.resetButton.grid(row=2, column=2)
        self.checkLabel.grid(row=3, column=1)

    def setTimerStateLabel(self) -> None:
        if self.state == States.NONE:
            self.timerStateLabel.configure(text="Timer", foreground=GREEN)
        elif self.state == States.WORK:
            self.timerStateLabel.configure(text="Work", foreground=RED)
        else:
            self.timerStateLabel.configure(text="Break", foreground=PINK)

    def formatSeconds(self, seconds:int) -> str:
        (min, sec) = divmod(seconds, 60)
        #this format is decimal first digit:and 2 digits for the seconds 00 -> 59 (based on the divmod result) using 0's padding
        return "{0:d}:{1:0>2d}".format(min, sec)

# ---------------------------- TIMER RESET ------------------------------- # 
    def startClick(self) -> None:
        self.endTimeInSeconds = WORK_MIN*60
        self.state = States.WORK
        self.setTimerStateLabel()
        self.updateCountdownText()
        self.updateTimer()

    def updateCountdownText(self) -> None:
        self.canvas.itemconfigure(self.timerCanvasText, text=self.formatSeconds(self.endTimeInSeconds))

    def updateTimer(self) -> None:
        self.endTimeInSeconds -= 1
        self.updateCountdownText()
        if self.endTimeInSeconds > 0:
            self.timerCancellationHandle = self.window.after(self.timerInterval, self.updateTimer)
        else:
            if self.state == States.WORK:
                self.completedPomodoros += 1
                if (self.completedPomodoros % 4 == 0):
                    self.state = States.LONG_BREAK
                    self.endTimeInSeconds = LONG_BREAK_MIN*60
                else:
                    self.state = States.BREAK
                    self.endTimeInSeconds = SHORT_BREAK_MIN*60
            else:
                self.state = States.WORK
                self.endTimeInSeconds = WORK_MIN*60

            self.setTimerStateLabel()
            self.timerCancellationHandle = self.window.after(self.timerInterval, self.updateTimer)
            checkLabelText = ""
            for _ in range(self.completedPomodoros):
                checkLabelText += CHECK
            self.checkLabel.configure(text=checkLabelText)

    def resetClick(self) -> None:
        self.endTimeInSeconds = 0
        self.window.after_cancel(self.timerCancellationHandle)
        self.checkLabel.configure(text="")
        self.completedPomodoros = 0
        self.state = States.NONE
        self.updateCountdownText()
        self.setTimerStateLabel()

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #