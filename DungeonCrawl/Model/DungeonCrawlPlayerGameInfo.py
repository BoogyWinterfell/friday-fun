from dataclasses import dataclass

from Abstract.PlayerGameInfo import PlayerGameInfo
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


@dataclass
class DungeonCrawlPlayerGameInfo(PlayerGameInfo):
    respawn_time: int
    grid: DungeonGrid
