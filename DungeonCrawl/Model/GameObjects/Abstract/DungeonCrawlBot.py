import abc
from dataclasses import dataclass
from typing import List

from Abstract.Bot import Bot
from Abstract.GameAction import GameAction
from DungeonCrawl.Model.DungeonCrawlBotInfo import DungeonCrawlBotInfo
from DungeonCrawl.Model.DungeonCrawlPlayerGameInfo import DungeonCrawlPlayerGameInfo


@dataclass
class DungeonCrawlBot(Bot, metaclass=abc.ABCMeta):
    info: DungeonCrawlBotInfo

    @abc.abstractmethod
    def play_round(self, game_info: DungeonCrawlPlayerGameInfo) -> List[GameAction]:
        pass
