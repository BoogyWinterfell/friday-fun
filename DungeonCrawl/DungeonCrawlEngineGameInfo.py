from queue import Queue
from typing import Dict

from Abstract.Bot import Bot
from Abstract.EngineGameInfo import EngineGameInfo
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


class DungeonCrawlEngineGameInfo(EngineGameInfo):
    def __init__(self, players: Dict[str, Bot], grid: DungeonGrid,
                 respawn_time=20, max_rounds=1000, round_number=0):
        super().__init__(players, max_rounds, round_number)
        self.respawn_time = respawn_time
        self.grid = grid
        # TODO: Implement death queue.
        # self.death_queue = {}

    def __str__(self):
        return "Round:" + str(self.round_number) + " Players:" + str(self.players)
