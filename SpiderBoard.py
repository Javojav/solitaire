import Board

class SpiderPile(Board.Pile):
    def __init__(self):
        super().__init__()

        self.moveRules = [self.checkSuit, self.cardsAreInOrder]
        self.stackCompleteRules = [self.checkSuit, self.cardsAreInOrder]


    def canReceive(self, cards):
        if super().canReceive(cards):
            return False

        if len(self) == 0:
            return True
        
        if cards[-1].card + 1 == self.topCard().card:
            return True
        
        return False

class SpiderBoard(Board.Board):
    def __init__(self):
        super().__init__()
        self.piles = [SpiderPile() for _ in range(10)]
