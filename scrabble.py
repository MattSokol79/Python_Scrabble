# Importing the Scrabble score dictionary
from score import Score

# Creating the Scrabble game class
class Scrabble(Score):
    def __init__(self, word):
        super().__init__() # Inherits score from Score
        self.word = word

    def scrabble_score(self):
        total_score = 0
    # Iterates over each letter in the word
        for i in self.word:
            # Turns the word into lowercase
            i = i.lower()
            #adds the score based on each letter
            total_score = total_score + self.score[i]
        return total_score

def main():
    # Asks the player to input a word
    word = input("Please provide a word\n=> ")

    # Assigning an object to the class to begin the process
    game = Scrabble(word.lower())

    # Prints the total score for the word
    print(f"Word Scored: {game.scrabble_score()} points")


if __name__ == "__main__":
    main()