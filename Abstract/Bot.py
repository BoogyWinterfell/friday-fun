import abc
from dataclasses import dataclass
from typing import List, Type

from Abstract.GameAction import GameAction
from Abstract.GameObject import GameObject
from Abstract.NamedObject import NamedObject
from Abstract.PlayerGameInfo import PlayerGameInfo


@dataclass
class Bot(NamedObject, metaclass=abc.ABCMeta):
    items: List[GameObject]

    @abc.abstractmethod
    def play_round(self, game_info: Type[PlayerGameInfo]) -> List[GameAction]:
        pass
