import Board

class SpiderPile(Board.Pile):
    def __init__(self):
        super().__init__()

        self.moveRules = [self.checkSuit, self.cardsAreInOrder]
        self.stackCompleteRules = [self.checkSuit, self.cardsAreInOrder]


    def canReceive(self, cards):
        if not super().canReceive(cards):
            return False

        if len(self) == 0:
            return True
        
        if cards[-1].card + 1 == self.topCard().card:
            return True
        
        return False

    def canRemove(self, amount):
        if super().canRemove(amount) == False:
            return False
        
        if self.pileStackIsComplete(amount, self.stackCompleteRules):
            return True
        
        return False
    
    def checkSuit(self, amount):
        if len(self) == 0 or amount == 1:
            return True

        if len(self) < amount:
            return False

        cardsToCheck = self.cards[:amount]

        for _, card in enumerate(cardsToCheck, start=1):
            if not card.faceUp and card.suit != self.topCard().suit:
                return False
            
        return True
    
    def cardsAreInOrder(self, amount):
        if len(self) == 0 or amount == 1:
            return True

        if len(self) < amount:
            return False
        
        cardsToCheck = self.cards[:amount]

        for idx, card in enumerate(cardsToCheck, start=1):
            if not card.faceUp and card.card != self.getCard(idx - 1).card + 1:
                return False
            
        return True
    

    def pileStackIsComplete(self, amount, rules=None):
        if len(self) == 0:
            return False
        
        if rules is None:
            rules = self.stackCompleteRules

        for rule in rules:
            if rule(amount) == False:
                return False
        
        return True
    

class SpiderBoard(Board.Board):
    def __init__(self):
        super().__init__()
        self.piles = [SpiderPile() for _ in range(10)]


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
    