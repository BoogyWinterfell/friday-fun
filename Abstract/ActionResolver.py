import abc
from typing import List, Type

from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo


class ActionResolver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def resolve_action(self, actions: List[GameAction], game_state: GameInfo) -> GameInfo:
        pass
