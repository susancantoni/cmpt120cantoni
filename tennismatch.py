# tennis match 
from player import Player

class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        self.receiver = self.playerB

    def play(self):
        # a match has three sets
        for i in range(3):
            while not self.isSetOver():
                while not self.isGameOver():
                    if self.server.winsServe():
                        self.server.incScore()
                    else:
                        self.receiver.incScore()
                        self.changeServer()
 #       print("final result: A won %d, B won %d" % (self.playerA.gamesWon, self.playerB.gamesWon)

    def getScores(self):
        #return number of sets won as 'score' for stats printout
        return self.playerA.setsWon, self.playerB.setsWon

    def isGameOver(self):
        #print("isGameOver: A %d B %d" % (self.playerA.score, self.playerB.score))
        if (self.playerA.score > 40 and (self.playerA.score - self.playerB.score >= 30)):
            self.playerA.gamesWon += 1
            self.playerA.score = 0
            self.playerB.score = 0
            return True
        elif (self.playerB.score > 40 and (self.playerB.score - self.playerA.score >= 30)):
            self.playerB.gamesWon += 1
            self.playerA.score = 0
            self.playerB.score = 0
            return True
        else:
            return False

    def isSetOver(self):
        # must win at least 6 games and be ahead by 2 games or more
        #print("isSetOver: A %d B %d" % (self.playerA.gamesWon, self.playerB.gamesWon))
        if (self.playerA.gamesWon >= 6 and (self.playerA.gamesWon - self.playerB.gamesWon >= 2)):
            self.playerA.setsWon += 1
            self.playerA.gamesWon = 0
            self.playerB.gamesWon = 0
            #print("player A wins set")
            return True
        elif (self.playerB.gamesWon >= 6 and (self.playerB.gamesWon - self.playerA.gamesWon >= 2)):
            self.playerB.setsWon += 1
            self.playerA.gamesWon = 0
            self.playerB.gamesWon = 0
            #print("player B wins set")
            return True
        else:
            return False

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
            self.receiver = self.playerA
        else:
            self.server = self.playerA
            self.receiver = self.playerB
    
