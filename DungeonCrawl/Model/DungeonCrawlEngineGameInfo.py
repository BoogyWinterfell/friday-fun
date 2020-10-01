from dataclasses import dataclass
from queue import Queue
from typing import Dict

from Abstract.Bot import Bot
from Abstract.EngineGameInfo import EngineGameInfo
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


@dataclass
class DungeonCrawlEngineGameInfo(EngineGameInfo):
    grid: DungeonGrid
    respawn_time: int
    # TODO: Implement death queue.
