import Cards
import json
import random

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
    
    def __len__(self):
        return len(self.cards)

class Board:
    def __init__(self):
        config = self.read_config('config.json')

        self.graphic = config['graphic']

        self.initialDeal = config['initialDeal']

        self.piles = [Pile() for _ in range(len(self.initialDeal))]

        self.deck = Cards.Deck(
            config['numberOfCards'], 
            config['suits'],
            config['rank'], 
        )

        self.completedStacks = 0

        self.gameOver = False

    

    def winCondition(self):
        if self.completedStacks == self.deck.amountOfCards//self.deck.rank:
            return True
        
        return False


    def startGame(self):
        # shuffles the cards
        self.deck.shuffle()

        # creates the piles
        self.dealCards(pattern=self.initialDeal)


    def dealCards(self, pattern=None):
        if pattern is None:
            pattern = [1 for _ in range(len(self.piles))]

        for i, pile in enumerate(self.piles):
            if pattern[i] > 0:
                cardFromDeck = self.deck.deal()

                if cardFromDeck is None:
                    pattern[i] = 0
                    break
                else:
                    pile.addCards(cardFromDeck)

                self.checkStackCompletion(pile)

                pattern[i] -= 1

        if sum(pattern) != 0:
            self.dealCards(pattern=pattern)
            
        self.turnTopCardsFaceUp()


    def turnTopCardsFaceUp(self):
        for pile in self.piles:
            pile.turnTopCardFaceUp()


    def moveCard(self, fromPile, toPile, amount):
        if not self.isMoveLegal(fromPile, toPile, amount):
            return False

        movedCards = self.piles[fromPile].removeCards(amount)
        self.piles[toPile].addCards(movedCards)

        self.piles[fromPile].turnTopCardFaceUp()

        self.piles[toPile] = self.checkStackCompletion(self.piles[toPile])

        return True


    def checkSuit(self, pile, amount):
        suit = pile[0].suit

        if len(pile) < amount:
            return False

        for i in range(amount):
            if pile[i].suit != suit:
                return False
            
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

        if len(self.piles[toPile]) == 0:
            return True

        if self.piles[toPile].canReceive(self.piles[fromPile].cards[:amount]):
            return True
        
        return False


    def checkStackCompletion(self, pile):
        if pile.pileStackIsComplete(self.deck.rank):
            self.completedStacks += 1
            pile.cards = []
        
        if self.winCondition():
            self.gameOver = True

        return pile
    

    def read_config(self, config_file):
        with open(config_file) as f:
            config = json.load(f)
        
        return config