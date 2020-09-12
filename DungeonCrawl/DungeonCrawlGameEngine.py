from typing import Tuple, List

from Abstract.ActionResolver import ActionResolver
from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.EngineGameInfo import EngineGameInfo


class DungeonCrawlGameEngine(GameEngine):
    def __init__(self, resolvers: List[ActionResolver]):
        self.resolvers = resolvers

    def resolve_actions(self, actions: Tuple[GameAction], game_state: EngineGameInfo):
        pass
