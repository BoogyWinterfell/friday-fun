from dataclasses import dataclass
from typing import List

from Abstract.BotInfo import BotInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject


@dataclass
class DungeonCrawlBotInfo(BotInfo):
    items: List[DungeonCrawlGameObject]
