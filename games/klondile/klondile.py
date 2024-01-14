import sys

if __name__ == "__main__":
    sys.path.append("../..")
    

from games.klondile import KlondileBoard
from games.klondile import klondileDisplay as klondileDisplay
from games.generic import Game


def klondileMain(config_file):
    game = Game.Game(KlondileBoard.klondileBoard, klondileDisplay.klondileDisplay)
    game.run(config_file)
    print("Work in progress")
    
if __name__ == "__main__":
    klondileMain("config.json")