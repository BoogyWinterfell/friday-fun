import abc
from dataclasses import dataclass
from typing import List

from Abstract.Bot import Bot
from Abstract.GameAction import GameAction
from DungeonCrawl.Model.DungeonCrawlPlayerGameInfo import DungeonCrawlPlayerGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject


@dataclass
class DungeonCrawlBot(Bot, metaclass=abc.ABCMeta):
    items: List[DungeonCrawlGameObject]

    @abc.abstractmethod
    def play_round(self, game_info: DungeonCrawlPlayerGameInfo) -> List[GameAction]:
        pass
