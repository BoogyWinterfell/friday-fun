from abc import ABC
from typing import List

from Abstract.GameInfo import GameInfo
from Abstract.WinCheck import WinCheck
from DungeonCrawl.DungeonCrawlGameInfo import DungeonCrawlGameInfo
from DungeonCrawl.DungeonCrawlUtils import get_dungeoneer_treasure_worth
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


class TreasureWinCheck(WinCheck, ABC):
    def __init__(self, treasure_to_win):
        self.treasure_to_win = treasure_to_win

    def search_for_winners(self, info: GameInfo) -> List[str]:
        game_info = DungeonCrawlGameInfo(**info.__dict__)

        winning_bots_names = [name for name, bot in game_info.players.items() if sum([
            worth for worth in [get_dungeoneer_treasure_worth(d) for d in bot.items if isinstance(d, Dungeoneer)]
        ]) >= self.treasure_to_win]

        return winning_bots_names
