from dataclasses import dataclass, field
from spacedRepetitionModel import SpacedRepetitionModel
import random
import operator

@dataclass
class FlashcardGameModel:
    source: str = ""
    questionHeading: str = ""
    answerHeading: str = ""
    models: list[SpacedRepetitionModel] = field(default_factory=list)
    indices: list[int] = field(default_factory=list)
    currentIndex: int = 0

    def GetCurrentIndex(self) -> int:
        return self.indices[self.currentIndex]

    def Randomize(self) -> None:
        indexDictionary = dict[int, list[int]]()
        #put all the stuff into the dictionary based on interval
        for i in range(len(self.models)):
            if indexDictionary.get(self.models[i].interval) == None:
                indexDictionary[self.models[i].interval] = list[int]()
            indexDictionary[self.models[i].interval].append(i)

        #this line needs some explanation
        #it sorts the keys into a new collection
        #since the keys are the intervals it's supposed to show you stuff
        #it effectively puts the stuff you get the most wrong in front
        sortedKeys = sorted(indexDictionary)

        toRemove = dict[int, list[int]]()
        for i in sortedKeys:
            if i > 0:
                # for each one we've actually managed to ever get right, <= 0 we've never gotten right
                for j in indexDictionary[i]:
                    # if it's been a while since we answered this one
                    if self.models[j].Include():
                        if indexDictionary.get(0) == None:
                            indexDictionary[0] = list[int]()
                        #put it in the 0 interval collection
                        indexDictionary[0].append(j)
                        if toRemove.get(i) == None:
                            toRemove[i] = list[int]()
                        #schedule it for removal from it's original spot
                        toRemove[i].append(j)

        #remove them after we've looped over them
        for i in toRemove:
            for j in toRemove[i]:
                indexDictionary[i].remove(j)

        #add the indices to the list with lowest intervals getting priority
        self.indices = list[int]()
        for i in sortedKeys:
            random.shuffle(indexDictionary[i])
            self.indices.extend(indexDictionary[i])
        
        self.currentIndex = 0

    def CurrentCard(self) -> SpacedRepetitionModel:
        return self.models[self.indices[self.currentIndex]]
    
    def NextCard(self) -> SpacedRepetitionModel:
        self.currentIndex = (self.currentIndex + 1) % len(self.models)
        return self.CurrentCard()
