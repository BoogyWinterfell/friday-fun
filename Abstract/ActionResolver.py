import abc

from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo


class ActionResolver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def resolve_action(self, action: GameAction, game_state: GameInfo):
        pass
