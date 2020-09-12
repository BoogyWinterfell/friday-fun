from Abstract.PlayerGameInfo import PlayerGameInfo
from DungeonCrawl.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo


class DungeonCrawlPlayerGameInfo(PlayerGameInfo):
    def __init__(self, game_info: DungeonCrawlEngineGameInfo):
        super().__init__(game_info)
