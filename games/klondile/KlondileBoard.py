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
        if self.completedStacks == self.deck.rank:
            return True
        
        return False