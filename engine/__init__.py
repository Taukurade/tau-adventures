
from .Player import Player
from .Utils import Map
from .Logger import Logger
class Game:
    def __init__(self) -> None:
        self.data = Map()
        pass

    def preload(self, player:Player):
        self.data.player = player