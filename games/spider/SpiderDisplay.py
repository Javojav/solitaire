import sys
import os
import math

from games.generic import display as genericDisplay

class SpiderDisplay(genericDisplay.Display):
    def __init__(self, board):
        super().__init__(board)

    def drawGameInfo(self):
        super().drawGameInfo()
        pileNumber = len(self.board.piles)
        sys.stdout.write(f"Completed Stacks: {self.board.completedStacks} \n")
        sys.stdout.write(f"Deals left: {math.ceil(len(self.board.deck.cards) / pileNumber) } \n\n")


    def drawRules(self):
        sys.stdout.write(
            """
        The main purpose of the game is to remove all cards
        from the table, assembling them in the tableau before 
        removing them.[3] Initially, 54 cards are dealt to the 
        tableau in ten piles, face down except for the top cards. 
        The tableau piles build down by rank, and in-suit sequences 
        can be moved together. The 50 remaining cards can be dealt to 
        the tableau ten at a time when none of the piles are empty.
        \n(Yes i fucking got it from Wikipedia)\n
        """
        )