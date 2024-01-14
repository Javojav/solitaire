import sys

if __name__ == "__main__":
    sys.path.append("../..")
    

from games.spider import SpiderBoard 
from games.spider import SpiderDisplay as display
from games.generic import Game


def spiderMain(config_file):
    game = Game.Game(SpiderBoard.SpiderBoard, display.SpiderDisplay)
    game.run(config_file)
    
if __name__ == "__main__":
    spiderMain("config.json")