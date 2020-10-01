import abc
from dataclasses import dataclass
from typing import Dict

from Abstract.Bot import Bot
from Abstract.GameInfoBase import GameInfoBase


@dataclass
class EngineGameInfo(GameInfoBase, metaclass=abc.ABCMeta):
    players: Dict[str, Bot]
