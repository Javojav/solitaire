import games.generic.display as display
import games.klondile.klondilePile as klondilePile
import sys

class klondileDisplay(display.Display):
    def __init__(self, board):
        super().__init__(board)


    def drawGameInfo(self):
        super().drawGameInfo()
        sys.stdout.write(f"Completed Stacks: {self.board.completedStacks} \n")
        sys.stdout.write(f"Deals left: {len(self.board.deck.cards)} \n\n")


    def drawJustTopCard(self):
        topCardPiles = []
        
        for pile in self.board.piles:
            if type(pile) == klondilePile.suitPile:
                topCardPiles.append(pile)
            
            if type(pile) == klondilePile.dealPile:
                topCardPiles.append(pile)

        return topCardPiles


    def drawWholePiles(self):
        wholePile = []

        for pile in self.board.piles:
            if type(pile) == klondilePile.klondilePile:
                wholePile.append(pile)


        return wholePile