import games.generic.Pile as Pile

class klondilePile(Pile.Pile):
    def __init__(self):
        super().__init__()

    def canReceive(self, cards):
        if len(self) == 0 and cards[-1].card == 13:
            return True

        if len(self) > 0 and cards[-1].card != self.topCard().card - 1:
            return False

        if len(self) > 0 and cards[-1].suit % 2 == (self.topCard().suit + 1) % 2:
            return True

        return False

class dealPile(Pile.Pile):
    def __init__(self):
        super().__init__()

    def canReceive(self, cards):
        return False

class suitPile(Pile.Pile):
    def __init__(self):
        super().__init__()

    def canReceive(self, cards):
        if len(self) == 0 and cards[-1].card == 1:
            return True

        if len(self) > 0 and cards[-1].card != self.topCard().card + 1:
            return False
        
        if len(self) > 0 and cards[-1].suit == self.topCard().suit:
            return True


        return False
    
    def pileStackIsComplete(self, rank):
        if len(self) == rank:
            return True

        return False