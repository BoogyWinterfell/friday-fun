from dataclasses import dataclass
from typing import List

from Abstract.EngineGameInfo import EngineGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlBot import DungeonCrawlBot
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


@dataclass
class DungeonCrawlEngineGameInfo(EngineGameInfo):
    grid: DungeonGrid
    respawn_time: int
    players: List[DungeonCrawlBot]
    # TODO: Implement death queue.
