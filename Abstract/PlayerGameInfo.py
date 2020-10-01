import abc
from dataclasses import dataclass

from Abstract.GameInfoBase import GameInfoBase


# This class prevents circular referencing between Bot and EngineGameInfo.
@dataclass
class PlayerGameInfo(GameInfoBase, metaclass=abc.ABCMeta):
    pass
