import abc
from dataclasses import dataclass
from typing import List

from Abstract.BotInfo import BotInfo
from Abstract.GameInfoBase import GameInfoBase


@dataclass
class GameInfo(GameInfoBase, metaclass=abc.ABCMeta):
    players: List[BotInfo]
