from dataclasses import dataclass

from flashcard import FlashCard
from datetime import datetime, timedelta
from time import time
from constants import *

@dataclass
class SpacedRepetitionModel:
    flashCard: FlashCard
    mostRecentCorrectAnswer: float = time()
    interval: int = 0

    def Include(self) -> bool:
        now = datetime.now()
        index = self.interval
        convertedTime = datetime.fromtimestamp(self.mostRecentCorrectAnswer)
        if index > len(INTERVALS):
            index = -1
        next = timedelta(minutes=INTERVALS[index])
        return (convertedTime + next < now)
