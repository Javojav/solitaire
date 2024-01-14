import random

class Card:
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit
        self.faceUp = False

class Deck:
    def __init__(self, amountOfCards, suits, ranks):
        self.rank = ranks
        self.amountOfCards = amountOfCards
        self.suits = suits

        self.cards = []

        duplicates = self.amountOfCards//self.rank//self.suits # cards that exist multiple times 
        if duplicates == 0:
            assert False, "Not enough cards for the given rank and suits"

        self.cards = [Card(card, suit) for _ in range(duplicates) for suit in range(self.suits) for card in range(1, self.rank+1)]


    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, amount=1, dealMinimum=True):
        if dealMinimum:
            amount = min(amount, len(self))

        if len(self) < amount or amount <= 0:
            return None
        
        return [self.cards.pop() for _ in range(amount)]
    
    def __len__(self):
        return len(self.cards)