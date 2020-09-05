from typing import List

from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo
from Abstract.GameObject import GameObject


class Bot:
    def __init__(self, items: List[GameObject] = None):
        self.items = items

    def play_round(self, game_info: GameInfo) -> List[GameAction]:
        pass
