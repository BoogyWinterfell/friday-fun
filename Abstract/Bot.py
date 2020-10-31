import abc
from dataclasses import dataclass
from typing import List, Type

from Abstract import BotInfo
from Abstract.GameAction import GameAction
from Abstract.NamedObject import NamedObject
from Abstract.PlayerGameInfo import PlayerGameInfo


@dataclass
class Bot(NamedObject, metaclass=abc.ABCMeta):
    info: BotInfo

    @abc.abstractmethod
    def play_round(self, game_info: Type[PlayerGameInfo]) -> List[GameAction]:
        pass
