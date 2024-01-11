import Board
import sys
import os
import math

colors = {
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

def clearScreen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def paintPileNumber(Numbers):
    for idx in range(Numbers):
        sys.stdout.write(f"{idx} ")

    sys.stdout.write("\n")


def drawBoard(board, message=""):
    graphic = board.graphic

    pileNumber = len(board.piles)

    sys.stdout.write("\033[H") # move cursor to top left
    sys.stdout.write(f"Completed piles: {board.completedPiles} \n")
    sys.stdout.write(f"Deals left: {math.ceil(len(board.cards) / pileNumber) } \n\n")
    
    if bool(graphic["PileNumberAtTheTop"]):
        paintPileNumber(pileNumber)
    
    sys.stdout.write("\n")

    largestPile = max([len(pile) for pile in board.piles])

    reversedPiles = [pile[::-1] for pile in board.piles]

    for i in range(largestPile):
        for pile in reversedPiles:
            length = len(pile)
            if i >= length:
                sys.stdout.write("  ")
            else:
                char = graphic["faces"][pile[i].card - 1] if pile[i].faceUp else graphic["back"]
                color = graphic["suitColors"][pile[i].suit] if pile[i].faceUp else graphic["backColor"]
                color = colors[color]
                sys.stdout.write(f"{color}{char} ")
        sys.stdout.write("\n")

    sys.stdout.write("\n")
    sys.stdout.write("\033[0m") # reset color

    if bool(graphic["PileNumberAtTheBottom"]):
        paintPileNumber(pileNumber)

    sys.stdout.write(f"{message}\n")
    sys.stdout.write(f"\nh for help: \n")
    sys.stdout.write(f"\nEnter move: \n")
    sys.stdout.flush()


def drawHelp():
    clearScreen()
    sys.stdout.write("\033[H") # move cursor to top left
    sys.stdout.write("\n")
    sys.stdout.write("Solitaire\n")
    sys.stdout.write("=========\n")
    sys.stdout.write("\n")
    sys.stdout.write("Rules\n")
    sys.stdout.write("-----")
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