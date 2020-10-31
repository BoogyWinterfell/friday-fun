from dataclasses import dataclass
from typing import List

from Abstract.PlayerGameInfo import PlayerGameInfo
from DungeonCrawl.Model.DungeonCrawlBotInfo import DungeonCrawlBotInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


@dataclass
class DungeonCrawlPlayerGameInfo(PlayerGameInfo):
    grid: DungeonGrid
    respawn_time: int
    players: List[DungeonCrawlBotInfo]
    game_objects: List[DungeonCrawlGameObject]
    # TODO: Implement death queue.
