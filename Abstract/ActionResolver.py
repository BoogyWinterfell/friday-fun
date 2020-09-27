import abc
from typing import List

from Abstract.GameAction import GameAction
from Abstract.EngineGameInfo import EngineGameInfo


class ActionResolver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def resolve_action(self, actions: List[GameAction], game_state: EngineGameInfo) -> EngineGameInfo:
        pass
