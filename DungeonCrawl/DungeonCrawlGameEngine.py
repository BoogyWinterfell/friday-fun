from typing import List, Dict

from Abstract.ActionResolver import ActionResolver
from Abstract.EngineGameInfo import EngineGameInfo
from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine


class DungeonCrawlGameEngine(GameEngine):
    def __init__(self, resolvers: List[ActionResolver]):
        self.resolvers = resolvers

    def resolve_actions(self, actions: Dict[str, List[GameAction]], game_state: EngineGameInfo):
        pass
