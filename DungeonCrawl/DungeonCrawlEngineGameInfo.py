from queue import Queue
from typing import Dict, List

from Abstract.Bot import Bot
from Abstract.EngineGameInfo import EngineGameInfo
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid
from DungeonCrawl.Model.GameObjects.Tile import Tile


class DungeonCrawlEngineGameInfo(EngineGameInfo):
    def __init__(self, players: Dict[str, Bot], tiles: List[Tile],
                 respawn_time=20, rows: int = 10, columns: int = 10,
                 max_rounds=1000, round_number=0):
        super().__init__(players, max_rounds, round_number)
        self.respawn_time = respawn_time
        self.grid = DungeonGrid(tiles, rows, columns)
        self.death_queue = Queue()
