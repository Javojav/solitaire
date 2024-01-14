import games.generic.Board as Board
import sys
import os
import math
    
class Display():
    def __init__(self, board):
        self.colors = {
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "black": "\033[30m",
            "reset": "\033[0m"
        }

        self.board = board
        self.graphic = self.board.graphic

    def clearScreen(self):
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

    def paintPileNumber(self, Numbers):
        for idx in range(Numbers):
            sys.stdout.write(f"{idx} ")

        sys.stdout.write("\n")
        sys.stdout.write("\n")

    def drawGame(self, board, message=""):
        self.board = board

        self.clearScreen()
        
        if self.graphic["PileNumberAtTheTop"]:
            self.paintPileNumber(len(self.board.piles))
        
        self.drawGameInfo()
        
        self.drawBoard()

        if self.graphic["PileNumberAtTheBottom"]:
            self.paintPileNumber(len(self.board.piles))
        
        self.drawMessage(message)

        self.drawInput()
    
    def drawMessage(self, message=""):
        sys.stdout.write(f"{message}\n")
        sys.stdout.write(f"\nh for help: \n\n")

    def drawInput(self):
        sys.stdout.write(f"Enter move: \n")
        sys.stdout.flush()

    def drawGameInfo(self):
        sys.stdout.write("\033[H") # move cursor to top left

    def drawBoard(self):
        largestPile = max([len(pile) for pile in self.board.piles])

        reversedPiles = [pile.cards[::-1] for pile in self.board.piles]

        for i in range(largestPile):
            for pile in reversedPiles:
                length = len(pile)
                
                card = None if i >= length else pile[i]
                if card == None:
                    sys.stdout.write("  ")
                else:
                    char = self.graphic["faces"][card.card - 1] if card.faceUp else self.graphic["back"]
                    color = self.graphic["suitColors"][card.suit] if card.faceUp else self.graphic["backColor"]
                    color = self.colors[color]
                    sys.stdout.write(f"{color}{char} ")
            sys.stdout.write("\n")
    
        sys.stdout.write("\n")
        sys.stdout.write("\033[0m") # reset color


    def drawRules(self):
        return


    def drawHelp(self):
        self.clearScreen()
        sys.stdout.write("\033[H") # move cursor to top left
        sys.stdout.write("\n")
        sys.stdout.write("Solitaire\n")
        sys.stdout.write("=========\n")
        sys.stdout.write("\n")
        sys.stdout.write("Rules\n")
        sys.stdout.write("-----")

        self.drawRules()
        
        sys.stdout.write("\n")
        sys.stdout.write("Controls")
        sys.stdout.write("\n--------")
        sys.stdout.write("\n")
        sys.stdout.write("    You control the game by entering text and pressing enter\n\n\n")
        sys.stdout.write("    Move (write a space after each argument): from to amount(optional 1 default)\n")
        sys.stdout.write("    Example: \n")
        sys.stdout.write("    \"1 2\" will move 1 card from pile 1 to pile 2\n")
        sys.stdout.write("    \"1 2 3\" will move 3 cards from pile 1 to pile 2\n\n")
        sys.stdout.write("    deal cards: d\n\n")
        sys.stdout.write("    restart: r\n\n")
        sys.stdout.write("    quit: q\n\n\n")

        sys.stdout.write("Press any key to get back...\n")