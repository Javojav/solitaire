import sys

if __name__ == "__main__":
    sys.path.append("../..")
    

from games.generic import Board as klondileBoard 
from games.generic import display as klondileDisplay
from games.generic import Game


def klondileMain(config_file):
    # game = Game.Game(klondileBoard.Board, klondileDisplay.Display)
    # game.run(config_file)
    print("Work in progress")
    
if __name__ == "__main__":
    klondileMain("config.json")