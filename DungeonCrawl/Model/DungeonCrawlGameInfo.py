from dataclasses import dataclass
from typing import List

from Abstract.GameInfo import GameInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlBot import DungeonCrawlBot
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


@dataclass
class DungeonCrawlGameInfo(GameInfo):
    grid: DungeonGrid
    respawn_time: int
    players: List[DungeonCrawlBot]
    # TODO: Implement death queue.
