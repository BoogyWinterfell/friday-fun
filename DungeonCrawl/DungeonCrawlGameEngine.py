from typing import Tuple

from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.GameInfo import GameInfo


class DungeonCrawlGameEngine(GameEngine):
    def __init__(self, max_rounds=1000, respawn_time=20):
        self.respawn_time = respawn_time
        self.max_rounds = max_rounds

    def resolve_actions(self, actions: Tuple[GameAction], game_state: GameInfo):
        pass
