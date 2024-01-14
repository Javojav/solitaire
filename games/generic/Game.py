import sys

if __name__ == "__main__":
    sys.path.append("../..")

import games.generic.Board as Board
import games.generic.display as Display

class Game():
    def __init__(self, boardConstructor, displayConstructor):
        self.boardConstructor = boardConstructor
        self.displayConstructor = displayConstructor

    def getInputs(self):
        inputs = input("")

        if inputs == "r":
            return "restart", None, None, None
        
        if inputs == "h":
            return "help", None, None, None
        
        if inputs == "q":
            return "quit", None, None, None
        
        if inputs == "d":
            return "deal", None, None, None

        if inputs.count(" ") >= 1:
            
            if inputs.count(" ") == 1:
                moveFrom, moveTo = inputs.split(" ")
                amount = "1"
            else:
                moveFrom, moveTo, amount = inputs.split(" ")

            if moveFrom.isdigit() and moveTo.isdigit() and amount.isdigit():
                return "move", int(moveFrom), int(moveTo), int(amount)

        return "error", None, None, None
    
    def controls(self, board, disp):
        action, fromPile, toPile, amount = self.getInputs()
        message = ""

        ret = True

        if action == "restart":
            board = self.boardConstructor("config.json")
            board.startGame()

        if action == "help":
            disp.drawHelp()
            input()

        if action == "deal":
            board.dealCards()
        elif action == "move":
            ret = board.moveCard(fromPile, toPile, amount)
        
        if action == "error" or ret == False:
            message = "Invalid!"

        if action == "quit":
            exit()

        return message, board, disp
    
    def run(self, configFile):
        board = self.boardConstructor(configFile)
        disp = self.displayConstructor(board)
        message=""

        board.startGame()

        while not board.gameOver:
            disp.drawGame(board, message)

            message, board, disp = self.controls(board, disp)

if __name__ == "__main__":
    game = Game(Board.Board, Display.Display)
    game.run(configFile="config.json")