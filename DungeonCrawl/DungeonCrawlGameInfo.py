from typing import List

from Abstract.GameInfo import GameInfo
from DungeonCrawl.DungeonGrid import DungeonGrid
from DungeonCrawl.Tile import Tile


class DungeonCrawlGameInfo(GameInfo):
    def __init__(self, players, tiles: List[Tile]):
        super().__init__(players)
        self.grid = DungeonGrid(tiles)
