from dataclasses import dataclass

from Abstract.PlayerGameInfo import PlayerGameInfo
from DungeonCrawl.Model.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid


@dataclass
class DungeonCrawlPlayerGameInfo(PlayerGameInfo):
    respawn_time: int
    grid: DungeonGrid

    @classmethod
    def from_engine_game_info(cls, info: DungeonCrawlEngineGameInfo):
        return cls(info.max_rounds, info.round_number, info.respawn_time, info.grid)
