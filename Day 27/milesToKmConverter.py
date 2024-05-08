import tkinter

class MilesToKmConverter:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.userMilesEntry = tkinter.Entry(width=10)
        self.milesLabel = tkinter.Label(text="Miles")
        self.isEqualToLabel = tkinter.Label(text="is equal to")
        self.outputLabel = tkinter.Label(text="0")
        self.kmLabel = tkinter.Label(text="Km")
        self.calculateButton = tkinter.Button(text="Calculate", command=self.doCalculation)
        self.configureUI()
        self.window.mainloop()

    def configureUI(self) -> None:
        self.window.title("Miles to Km Converter")
        self.window.configure(padx=20, pady=20)
        self.userMilesEntry.insert(tkinter.END, "0")
        self.userMilesEntry.grid(row=0, column=1)
        self.milesLabel.grid(row=0,column=2)
        self.isEqualToLabel.grid(row=1,column=0)
        self.outputLabel.grid(row=1,column=1)
        self.kmLabel.grid(row=1,column=2)
        self.calculateButton.grid(row=2, column=1)

    def doCalculation(self) -> None:
        converted = float(self.userMilesEntry.get()) * 1.609344
        self.outputLabel.configure(text=f"{converted}")

