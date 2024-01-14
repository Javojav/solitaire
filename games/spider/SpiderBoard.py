from games.generic import Board as Board
from games.spider import SpiderPile as SpiderPile

class SpiderBoard(Board.Board):
    def __init__(self, config_file="games/spider/config.json"):
        super().__init__(config_file)
        self.piles = [SpiderPile.SpiderPile() for _ in range(len(self.initialDeal))]


    def winCondition(self):
        if self.completedStacks == self.deck.amountOfCards//self.deck.rank:
            return True
        
        return False


    def afterMove(self, fromPile, toPile, amount):
        self.piles[toPile] = self.checkStackCompletion(self.piles[toPile])


    def afterDeal(self):

        for pile in self.piles:
            self.checkStackCompletion(pile)


    def checkStackCompletion(self, pile):
        if pile.pileStackIsComplete(self.deck.rank):
            self.completedStacks += 1
            pile.cards = []
        
        if self.winCondition():
            self.gameOver = True

        return pile