from tkinter import *
from tkinter import filedialog, messagebox
from typing import Callable

class SetupForm:
    def __init__(self, root:Tk, closeEventHandler:Callable[[], None]) -> None:
        self.onCloseEventHandler = closeEventHandler
        self.source = ""
        self.questionHeading = ""
        self.answerHeading = ""
        self.saveLocation = ""

        self.root = root
        self.dialog = Toplevel(self.root)
        self.dialog.withdraw()
        self.dialog.title("Import Flashcard Deck")
        self.lblQuestionHeading = Label(self.dialog, text="Question Heading:")
        self.txtQuestionHeading = Entry(self.dialog)
        self.lblAnswerHeading = Label(self.dialog, text="Answer Heading:")
        self.txtAnswerHeading = Entry(self.dialog)
        self.lblSaveLocation = Label(self.dialog, text="SaveFile Name:")
        self.txtSaveLocation = Entry(self.dialog)
        self.btnSaveLocation = Button(self.dialog, text="💾", command=self.showFileDialog)
        self.btnOk = Button(self.dialog, text="OK", command=self.dismiss)
        self.setupUI()

    def setupUI(self) -> None:
        self.lblQuestionHeading.grid(row=0, column=0)
        self.lblQuestionHeading.focus()
        self.txtQuestionHeading.grid(row=0, column=1, columnspan=2, sticky="EW")
        self.lblAnswerHeading.grid(row=1, column=0)
        self.txtAnswerHeading.grid(row=1, column=1, columnspan=2, sticky="EW")
        self.lblSaveLocation.grid(row=2, column=0)
        self.txtSaveLocation.grid(row=2, column=1)
        self.btnSaveLocation.grid(row=2, column=2, padx=3)
        self.btnOk.grid(row=3, column=1, columnspan=2, sticky="EW", pady=5, padx=2)

    def showFileDialog(self) -> None:
        saveLocation = filedialog.asksaveasfilename(filetypes=[("Flashcard Game Model",".json")])
        if not saveLocation.endswith(".json"):
            saveLocation += ".json"
        self.txtSaveLocation.insert(END, saveLocation)

    def dismiss(self) -> None:
        self.questionHeading = self.txtQuestionHeading.get()
        self.answerHeading = self.txtAnswerHeading.get()
        self.saveLocation = self.txtSaveLocation.get()
        if self.questionHeading.strip() == "" or self.answerHeading.strip() == "" or self.saveLocation.strip() == "":
            messagebox.showwarning(title="All fields are required", message="Please fill out the form completely")
            return
        if not self.saveLocation.endswith(".json"):
            self.saveLocation += ".json"
        self.dialog.grab_release()
        self.dialog.destroy()
        self.onCloseEventHandler()
    
    def showDialog(self) -> None:
        self.source = filedialog.askopenfilename(filetypes=[("Flashcard Definition File", ".csv")])
        self.dialog.deiconify()
        self.dialog.protocol("WM_DELETE_WINDOW", self.dismiss) #intercept close button
        self.dialog.transient(self.root) #dialog window is related to main
        self.dialog.wait_visibility() #can't grab until window appears, so we wait
        self.dialog.grab_set() #ensure all input goes to our dialog
        self.dialog.wait_window() #block until window is destroyed
