from typing import List

from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo


class Bot:
    def play_round(self, game_info: GameInfo) -> List[GameAction]:
        pass
