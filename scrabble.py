# Importing the Scrabble score dictionary
from score import Score

# Creating the Scrabble game class
class Scrabble(Score):
    def __init__(self, word):
        super().__init__() # Inherits score from Score
        self.word = word

    def scrabble_score(self):
        total_score = 0

        for i in self.word:
            i = i.lower()
            total_score = total_score + self.score[i]
        return total_score

