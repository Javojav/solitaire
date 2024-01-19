import games.generic.Board as Board
import games.klondile.klondilePile as klondilePile

class klondileBoard(Board.Board):
    def __init__(self, config_file="games/klondile/config.json"):
        super().__init__(config_file)

        self.piles = [klondilePile.dealPile()]
        self.piles = self.piles + [klondilePile.klondilePile() for _ in range(len(self.initialDeal) - 1)]
        self.piles = self.piles + [klondilePile.suitPile() for _ in range(self.deck.suits)]
        
        self.NormalDeal = [self.config['cardsPerDeal']]


    def winCondition(self):
        if self.completedStacks == self.deck.suits:
            return True
        
        return False
    

    def afterMove(self, fromPile, toPile, amount):
        return self.checkPiles()


    def checkPiles(self):
        suitPiles = [pile for pile in self.piles if type(pile) == klondilePile.suitPile]
        
        for pile in suitPiles:
            if pile.pileStackIsComplete(self.deck.rank):
                self.completedStacks += 1
            
            if self.winCondition():
                self.gameOver = True

        return self.piles


    def dealCards(self, pattern=None):
        if len(self.deck) == 0:
            dealPile = self.piles[0]
            self.deck.addCards(dealPile.cards)
            dealPile.removeCards(len(dealPile))

        return super().dealCards(pattern)