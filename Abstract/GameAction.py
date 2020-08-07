import abc

from Abstract.GameInfo import GameInfo


class GameAction(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, game: GameInfo):
        pass
