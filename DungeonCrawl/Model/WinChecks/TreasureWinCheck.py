from abc import ABC
from typing import List

from Abstract.EngineGameInfo import EngineGameInfo
from Abstract.WinCheck import WinCheck
from DungeonCrawl.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.DungeonCrawlUtils import get_dungeoneer_treasure_worth
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


class TreasureWinCheck(WinCheck, ABC):
    def __init__(self, treasure_to_win):
        self.treasure_to_win = treasure_to_win

    def search_for_winners(self, info: EngineGameInfo) -> List[str]:
        # # Filter out the attributes that we don't give to the ctor.
        # desired_dict = {key: val for key, val
        #                 in info.__dict__.items()
        #                 if key != 'round_number' and key != 'death_queue'}
        # game_info = DungeonCrawlEngineGameInfo(**desired_dict)
        winning_bots_names = [name for name, bot in info.players.items() if sum([
            worth for worth in [get_dungeoneer_treasure_worth(d) for d in bot.items if d is Dungeoneer]
        ]) >= self.treasure_to_win]

        return winning_bots_names
