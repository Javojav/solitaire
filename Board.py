import json
import random

class Card:
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit
        self.faceUp = False
    

class Board:
    def __init__(self):
        config = self.read_config('config.json')

        self.suits = config['suits']
        self.graphic = config['graphic']

        self.initialDeal = config['initialDeal']
        self.piles = [[] for _ in range(len(self.initialDeal))]

        self.rank = config['rank'] # rank of the cards
        self.numberOfCards = config['numberOfCards']

        duplicates = self.numberOfCards//self.rank//self.suits # cards that exist multiple times 
        self.cards = [Card(card, suit) for _ in range(duplicates) for suit in range(self.suits) for card in range(1, self.rank+1)]

        self.completedPiles = 0

        self.gameOver = False


    def startGame(self):
        # shuffles the cards
        random.shuffle(self.cards)

        # creates the piles
        self.dealCards(pattern=self.initialDeal)


    def dealCards(self, pattern=None):
        if pattern is None:
            pattern = [1 for _ in range(len(self.piles))]

        for i, pile in enumerate(self.piles):
            if pattern[i] > 0:
                if len(self.cards) <= 0:
                    self.turnOverBottomCards()
                    return
                pile.insert(0, self.cards.pop())
                self.checkPileCompletion(pile)
                pattern[i] -= 1
        if sum(pattern) != 0:
            self.dealCards(pattern=pattern)
        
        self.turnOverBottomCards()


    def turnOverBottomCards(self):
        for pile in self.piles:
            if len(pile) > 0:
                pile[0].faceUp = True

    def moveCard(self, fromPile, toPile, amount):
        if not self.isMoveLegal(fromPile, toPile, amount):
            return False
        
        self.piles[toPile] = self.piles[fromPile][:amount] + self.piles[toPile]
        self.piles[fromPile] = self.piles[fromPile][amount:]

        if len(self.piles[fromPile]) > 0:
            self.piles[fromPile][0].faceUp = True

        self.piles[toPile] = self.checkPileCompletion(self.piles[toPile])

        return True


    def isMoveLegal(self, fromPile, toPile, amount):
        if fromPile < 0 or fromPile > len(self.piles) - 1:
            return False

        if toPile < 0 or toPile > len(self.piles) - 1:
            return False

        if fromPile == toPile:
            return False

        if amount > len(self.piles[fromPile]):
            return False
        
        suit = self.piles[fromPile][0].suit
        for i in range(amount):
            if self.piles[fromPile][i].suit != suit:
                return False

        for i in range(amount):
            if self.piles[fromPile][i].faceUp == False:
                return False

            if i > 0 and self.piles[fromPile][i].card != self.piles[fromPile][i-1].card + 1:
                return False

        if len(self.piles[toPile]) == 0:
            return True

        if self.piles[fromPile][amount - 1].card + 1 == self.piles[toPile][0].card:
            return True
        
        return False


    def checkPileCompletion(self, pile):
        ranksum = sum([val for val in range(1, self.rank+1)])

        suit = pile[0].suit
        sumacion = 0
        for idx, card in enumerate(pile):
            if idx > self.rank:
                break

            if card.faceUp == False:
                break

            if card.suit != suit:
                break
            sumacion += card.card

        if sumacion == ranksum:
            self.completedPiles += 1
            pile = pile[self.rank - 1:]

            if self.completedPiles == self.numberOfCards//self.rank:
                self.gameOver = True


        return pile
    

    def read_config(self, config_file):
        with open(config_file) as f:
            config = json.load(f)
        
        return config