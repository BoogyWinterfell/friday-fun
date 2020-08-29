from typing import List

from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo
from DungeonCrawl.Model.GameObjects.Abstract.Item import Item


class Bot:
    def __init__(self, items: List[Item] = None):
        self.items = items

    def play_round(self, game_info: GameInfo) -> List[GameAction]:
        pass
