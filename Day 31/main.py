# from flashcardIO import *
# from flashcardGameModel import *

# gameModel = FlashcardGameModel(source = r"data/japanese high frequency words.csv")

# flashCards = FlashcardIO.loadFlashCards("Japanese", "English", gameModel.source)
# gameModel.models = FlashcardIO.createSpacedRepetitionModels(flashCards)
# FlashcardIO.saveFlashCardGameModel(gameModel, r"data/data.json")

# gameModel = FlashcardIO.loadFlashCardGameModel("data.json")

from flashcardMainForm import FlashcardMainForm

form = FlashcardMainForm()