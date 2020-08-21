from typing import Dict, List

from Abstract.Bot import Bot
from Abstract.GameInfo import GameInfo
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid
from DungeonCrawl.Model.GameObjects.Tile import Tile


class DungeonCrawlGameInfo(GameInfo):
    def __init__(self, players: Dict[str, Bot], tiles: List[Tile], max_rounds=1000, respawn_time=20):
        super().__init__(players)
        self.respawn_time = respawn_time
        self.grid = DungeonGrid(tiles)
        self.max_rounds = max_rounds
