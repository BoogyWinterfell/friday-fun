from dataclasses import dataclass
from typing import List

from Abstract.GameAction import GameAction
from Abstract.PlayerGameInfo import PlayerGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlBot import DungeonCrawlBot


@dataclass
class DumbBot(DungeonCrawlBot):
    def play_round(self, game_info: PlayerGameInfo) -> List[GameAction]:
        pass
