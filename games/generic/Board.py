import games.generic.Cards as Cards
import games.generic.Pile as Pile
import json
import random

class Board:
    def __init__(self, config_file):
        self.config = self.read_config(config_file)
        self.config_file = config_file

        self.graphic = self.config['graphic']

        self.initialDeal = self.config['initialDeal']
        self.NormalDeal = [1 for _ in range(len(self.initialDeal))]

        self.piles = [Pile.Pile() for _ in range(len(self.initialDeal))]

        self.deck = Cards.Deck(
            self.config['numberOfCards'], 
            self.config['suits'],
            self.config['rank'], 
        )

        self.completedStacks = 0

        self.gameOver = False


    def winCondition(self):
        return False


    def startGame(self):
        # shuffles the cards
        self.deck.shuffle()

        # creates the piles
        self.dealCards(pattern=self.initialDeal)


    def dealCards(self, pattern=None):
        if pattern is None:
            pattern = [x for x in self.NormalDeal]

        if len(pattern) != len(self.piles):
            pattern.extend([0 for _ in range(len(self.piles) - len(pattern))])

        for i, pile in enumerate(self.piles):
            if pattern[i] > 0:
                cardFromDeck = self.deck.deal()

                if cardFromDeck is None:
                    pattern[i] = 0
                    break
                else:
                    pile.addCards(cardFromDeck)

                pattern[i] -= 1
            
        if sum(pattern) != 0:
            self.dealCards(pattern=pattern)
            
        self.turnTopCardsFaceUp()
        self.afterDeal()


    def afterDeal(self):
        pass
    

    def turnTopCardsFaceUp(self):
        for pile in self.piles:
            pile.turnTopCardFaceUp()


    def afterMove(self, fromPile, toPile, amount):
        pass


    def moveCard(self, fromPile, toPile, amount):
        if not self.isMoveLegal(fromPile, toPile, amount):
            return False

        movedCards = self.piles[fromPile].removeCards(amount)
        self.piles[toPile].addCards(movedCards)

        self.piles[fromPile].turnTopCardFaceUp()

        self.afterMove(fromPile, toPile, amount)

        return True
    

    def pileExists(self, pile):
        if pile < 0 or pile > len(self.piles) - 1:
            return False

        return True


    def isMoveLegal(self, fromPile, toPile, amount):
        if not self.pileExists(fromPile) or not self.pileExists(toPile): # if the pile does not exist
            return False

        if fromPile == toPile: # if the pile is the same
            return False

        if amount > len(self.piles[fromPile]): # if the amount of cards to move is greater than the amount of cards in the pile
            return False
        
        if not self.piles[fromPile].canRemove(amount): # if the pile is complete
            return False

        if self.piles[toPile].canReceive(self.piles[fromPile].cards[:amount]):
            return True
        
        return False
    
    def read_config(self, config_file):
        with open(config_file) as f:
            config = json.load(f)
        
        return config