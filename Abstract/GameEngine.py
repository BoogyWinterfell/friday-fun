import abc
from typing import List, Dict

from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo


class GameEngine(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def resolve_actions(self, actions: Dict[str, List[GameAction]], game_state: GameInfo):
        pass
