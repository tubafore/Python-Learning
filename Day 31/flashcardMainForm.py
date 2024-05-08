from threading import Timer
from time import time
from tkinter import *
from tkinter import filedialog
from setupForm import SetupForm
from flashcardIO import FlashcardIO
from flashcardGameModel import FlashcardGameModel
from setupForm import SetupForm
from mruModel import MruModel
from constants import *
from PIL import Image, ImageTk

import json
import random


class FlashcardMainForm:
    def __init__(self) -> None:
        self.model = FlashcardGameModel()
        self.modelPath = ""
        # UI stuff #
        self.root = Tk()
        self.root.title("Flashcards!")
        self.images = dict[str, ImageTk.PhotoImage]()
        self.loadImages()
        #highlightthickness = border (and is a super long way of saying border)
        self.cardCanvas = Canvas(self.root, highlightthickness=0, height=526, width=800, background=BACKGROUND_COLOR)
        self.headingLabel = 0
        self.qaLabel = 0
        self.imageOnCanvas = 0
        self.rightButton = Button(self.root, highlightthickness=0, command=self.correct, image=self.images["right"])  
        self.wrongButton = Button(self.root, highlightthickness=0, command=self.incorrect, image=self.images["wrong"]) 
        # this must be done before you start creating menus
        # otherwise you can "tear off" the menu and open it in its own window
        self.root.option_add("*tearOff", FALSE) 
        self.menubar = Menu(self.root)
        self.fileMenu = Menu(self.menubar)
        self.recent = Menu(self.fileMenu)
        self.root['menu'] = self.menubar     
        self.mruDecks = self.loadMru()
        self.setupUI()
        self.loadMruMenuItems()
        self.timer = Timer(0,self.doNothing)
        if len(self.model.models) > 0:
            self.loadFront()
        self.root.mainloop()

    def doNothing(self) -> None:
        pass

    def loadImages(self) -> None:
        load_rightImage = Image.open("images/right.png")
        load_wrongImage = Image.open("images/wrong.png")
        load_backImage = Image.open("images/card_back.png")
        load_frontImage = Image.open("images/card_front.png")
        self.images = {
            "back" : ImageTk.PhotoImage(load_backImage),
            "front" : ImageTk.PhotoImage(load_frontImage),
            "right" : ImageTk.PhotoImage(load_rightImage),
            "wrong" : ImageTk.PhotoImage(load_wrongImage)
        }

    def setupUI(self) -> None:
        self.root.configure(padx=50, pady=50, background=BACKGROUND_COLOR)
        self.root.geometry("900x700")
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.fileMenu.add_command(label="Open", command=self.openDeck)
        self.fileMenu.add_cascade(menu=self.recent, label="Open Recent")
        self.fileMenu.add_command(label="Import", command=self.importDeck)
        self.fileMenu.add_command(label="Save", command=self.saveDeck)
        self.fileMenu.add_command(label="Save As", command=self.saveDeckAs)
        self.fileMenu.add_command(label="Exit", command=self.onClose)
        self.imageOnCanvas = self.cardCanvas.create_image(400, 263, image=self.images["front"])
        self.cardCanvas.grid(row=0, column=0, columnspan=2)
        self.headingLabel = self.cardCanvas.create_text(400, 150, text="Heading", font=("Ariel", 40, "italic"))
        self.qaLabel = self.cardCanvas.create_text(400, 263, text="Question/Answer", font=("Ariel", 40, "bold"), width=700)

        self.wrongButton.grid(row=1, column=0)
        self.rightButton.grid(row=1, column=1)
        self.root.protocol("WM_DELETE_WINDOW", self.onClose) #intercept close button

    def onClose(self) -> None:
        self.saveDeck()
        self.timer.cancel()
        self.root.grab_release()
        self.root.destroy()

    def loadMru(self) -> MruModel:
        try:
            with open(file=MRU_PATH, mode="r") as file:
                modelDict = json.load(file)
                mruModel = MruModel(files=modelDict["files"])
                if len(mruModel.files) > 0:
                    self.modelPath = mruModel.files[0]
                    self.model = FlashcardIO.loadFlashCardGameModel(self.modelPath)
                    self.afterLoading()
                return mruModel
        except OSError:
            return MruModel(files=list[str]())
        except json.decoder.JSONDecodeError:
            return MruModel(files=list[str]())

    def loadMruMenuItems(self) -> None:
        #clear the old stuff
        if len(self.mruDecks.files) > 0:
            self.recent.delete(0, "end")
            for f in self.mruDecks.files:
                self.recent.add_command(label=f, command=lambda f=f: self.loadDeck(f))
    
    def pushMru(self, entry:str) -> None:
        #if it's in the MRU collection, move it to the top
        if entry in self.mruDecks.files:
            index = self.mruDecks.files.index(entry)
            #if it's already the first entry, it's in the right spot
            if index != 0:
                self.mruDecks.files.insert(0, self.mruDecks.files.pop(index))
                self.saveMru()

        #otherwise, just insert it at the top
        else:
            self.mruDecks.files.insert(0, entry)
            self.saveMru()
        

    def saveMru(self) -> None:
        with open(file=MRU_PATH, mode="w") as file:
            json.dump(fp=file, obj=self.mruDecks, indent=4, default=vars)
        self.loadMruMenuItems()

    def openDeck(self) -> None:
        self.modelPath = filedialog.askopenfilename(filetypes=[("Flashcard Deck File", ".json")])
        if self.modelPath != '':
            self.loadDeck(self.modelPath)
            if self.model == None:
                self.openDeck()
            

    def loadDeck(self, path:str) -> None:
        self.model = FlashcardIO.loadFlashCardGameModel(path)
        self.afterLoading()
        self.loadFront()
        self.pushMru(path)

    def afterLoading(self) -> None:
        self.model.Randomize()

    def importDeck(self) -> None:
        self.setupForm = SetupForm(self.root, self.setupFormClose)
        self.setupForm.showDialog()
        self.loadFront()

    def saveDeck(self) -> None:
        FlashcardIO.saveFlashCardGameModel(self.model, self.modelPath)
        self.pushMru(self.modelPath)

    def saveDeckAs(self) -> None:
        self.modelPath = filedialog.askopenfilename(filetypes=[("Flashcard Deck File", ".json")])
        self.saveDeck()

    def setupFormClose(self) -> None:
        self.model = FlashcardGameModel(self.setupForm.source, questionHeading=self.setupForm.questionHeading, answerHeading=self.setupForm.answerHeading)
        flashCards = FlashcardIO.loadFlashCards(self.model.questionHeading, self.model.answerHeading, self.model.source)
        self.model.models = FlashcardIO.createSpacedRepetitionModels(flashCards)
        FlashcardIO.saveFlashCardGameModel(self.model, self.setupForm.saveLocation)
        self.modelPath = self.setupForm.saveLocation
        self.pushMru(self.modelPath)

    def correct(self) -> None:
        self.model.models[self.model.GetCurrentIndex()].mostRecentCorrectAnswer = time()
        self.model.models[self.model.GetCurrentIndex()].interval += 1
        self.model.NextCard()
        self.loadFront()

    def incorrect(self) -> None:
        self.model.models[self.model.GetCurrentIndex()].interval -= 1
        self.model.NextCard()
        self.loadFront()

    def loadFront(self) -> None:
        self.cardCanvas.itemconfig(self.imageOnCanvas, image=self.images["front"])
        self.cardCanvas.itemconfig(self.headingLabel, text=self.model.questionHeading)
        self.cardCanvas.itemconfig(self.qaLabel, text=self.model.CurrentCard().flashCard.questionText)
        self.rightButton["state"] = 'disabled'
        self.wrongButton["state"] = 'disabled'
        self.timer = Timer(3.0, self.loadBack)
        self.timer.start()

    def loadBack(self) -> None:
        self.cardCanvas.itemconfig(self.imageOnCanvas, image=self.images["back"])
        self.cardCanvas.itemconfig(self.headingLabel, text=self.model.answerHeading)
        self.cardCanvas.itemconfig(self.qaLabel, text=self.model.CurrentCard().flashCard.answerText)
        self.rightButton["state"] = 'normal'
        self.wrongButton["state"] = 'normal'

