from typing import List

from Abstract.EngineGameInfo import EngineGameInfo
from Abstract.WinCheck import WinCheck
from DungeonCrawl.DungeonCrawlUtils import get_dungeoneer_treasure_worth
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


class TreasureWinCheck(WinCheck):
    def __init__(self, treasure_to_win):
        self.treasure_to_win = treasure_to_win

    def search_for_winners(self, info: EngineGameInfo) -> List[str]:
        winning_bots_names = [name for name, bot in info.players.items() if sum([
            worth for worth in [get_dungeoneer_treasure_worth(d) for d in bot.items if d is Dungeoneer]
        ]) >= self.treasure_to_win]

        return winning_bots_names
