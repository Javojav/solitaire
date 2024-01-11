import Board
import display


def getInputs():
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


def controls(board):
    action, fromPile, toPile, amount = getInputs()
    message = ""

    ret = True

    if action == "restart":
        board = Board.Board()
        board.startGame()

    if action == "help":
        display.drawHelp()
        input()

    if action == "deal":
        board.dealCards()
    elif action == "move":
        ret = board.moveCard(fromPile, toPile, amount)
    
    if action == "error" or ret == False:
        message = "Invalid!"

    if action == "quit":
        exit()

    return message, board


def main():
    board = Board.Board()
    board.startGame()
    message = ""


    while not board.gameOver:
        display.clearScreen()
        display.drawBoard(board, message)
        message, board = controls(board)
    
    print("K pro")

if __name__ == '__main__':
    main()