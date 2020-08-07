from Abstract.GameInfo import GameInfo
from DungeonCrawl.DungeonGrid import DungeonGrid


class DungeonCrawlGameInfo(GameInfo):
    def __init__(self, players):
        super().__init__(players)
        self.grid = DungeonGrid()
