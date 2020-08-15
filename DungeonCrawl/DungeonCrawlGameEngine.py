from typing import Tuple

from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.GameInfo import GameInfo


class DungeonCrawlGameEngine(GameEngine):
    def resolve_actions(self, actions: Tuple[GameAction], game_state: GameInfo):
        pass
