
class Pile:
    def __init__(self):
        self.cards = []

        self.moveRules = []
        self.stackCompleteRules = []

    
    def addCards(self, cards):
        if type(cards) is not list:
            cards = [cards]

        self.cards = cards + self.cards

    def removeCards(self, amount=1, index=0):
        removed = self.cards[index:index+amount]

        self.cards = self.cards[index+amount:]
        
        return removed


    def canReceive(self, cards):
        if type(cards) is not list:
            cards = [cards]

        if len(cards) < 1:
            return False
        
        return True


    def canRemove(self, amount):
        if len(self) == 0:
            return False

        if len(self) < amount:
            return False
        
        return True

    def topCard(self):
        return self.getCard(0)
    
    def getCard(self, index):
        if len(self) == 0 or index > len(self) - 1:
            return None

        return self.cards[index]
        
    def turnTopCardFaceUp(self):
        if self.topCard() is not None:
            self.topCard().faceUp = True
    
    def __len__(self):
        return len(self.cards)