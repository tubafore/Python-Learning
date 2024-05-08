import json
from typing import Callable
import pandas
import os
from flashcard import FlashCard
from flashcardGameModel import FlashcardGameModel
from spacedRepetitionModel import SpacedRepetitionModel
from tkinter import filedialog, messagebox


class FlashcardIO:
    def __init__(self) -> None:
        pass

    @staticmethod
    def loadFlashCards(questionHeading:str, answerHeading:str, pathToCSV:str) -> list[FlashCard]:
        csv = pandas.read_csv(pathToCSV)
        result = [FlashCard(questionText=item[1][questionHeading],answerText=item[1][answerHeading]) for item in csv.iterrows()]
        return result

    @staticmethod
    def createSpacedRepetitionModels(flashCards:list[FlashCard]) -> list[SpacedRepetitionModel]:
        result = [SpacedRepetitionModel(flashCard=item) for item in flashCards]
        return result
    
    @staticmethod
    def saveFlashCardGameModel(model:FlashcardGameModel, path:str) -> None:
        with open(file=path, mode="w") as file:
            json.dump(model, fp=file, indent=4, default=vars)

    # @staticmethod 
    # def createFlashCardGameModel() -> FlashcardGameModel:
    #     source = filedialog.askopenfilename(defaultextension="*.csv")
    #     model = FlashcardGameModel(source=source, questionHeading="Japanese", answerHeading="English")

    #     flashCards = FlashcardIO.loadFlashCards(model.questionHeading, model.answerHeading, model.source)
    #     model.models = FlashcardIO.createSpacedRepetitionModels(flashCards)
    #     FlashcardIO.saveFlashCardGameModel(model, r"data/data.json")
    #     return model

    @staticmethod
    def loadFlashCardGameModel(path:str) -> FlashcardGameModel:
        try:
            with open(file=path, mode="r") as file:
                modelDict = json.load(file)
                models = [SpacedRepetitionModel(flashCard=FlashCard(questionText=item["flashCard"]["questionText"], \
                        answerText=item["flashCard"]["answerText"]), mostRecentCorrectAnswer = item["mostRecentCorrectAnswer"], interval=item["interval"]) for item in modelDict["models"]]
                model = FlashcardGameModel(source=modelDict["source"], models=models, questionHeading=modelDict["questionHeading"], answerHeading=modelDict["answerHeading"])
                return model
        except OSError:
            messagebox.showinfo(title="Sorry...", message="The file failed to load, please try again or select a different file")
            return None