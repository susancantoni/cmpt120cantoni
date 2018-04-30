# tennis player
from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.gamesWon = 0
        self.setsWon = 0

    def winsServe(self):
        # Returns true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a point to this player's score. note beyond 40 just keep adding 15
        # because this is just an internal number (not real tennis score)
        if self.score == 30:
            self.score = self.score + 10
        else:
            self.score = self.score + 15

    def getScore(self):
        # Return this player's current score
        return self.score

