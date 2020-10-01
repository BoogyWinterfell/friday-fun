import abc
from typing import List

from Abstract.GameAction import GameAction
from Abstract.GameObject import GameObject
from Abstract.PlayerGameInfo import PlayerGameInfo


class Bot(metaclass=abc.ABCMeta):
    def __init__(self, items: List[GameObject] = None):
        if items is None:
            self.items = []
        else:
            self.items = items

    @abc.abstractmethod
    def play_round(self, game_info: PlayerGameInfo) -> List[GameAction]:
        pass
