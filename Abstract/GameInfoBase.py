import abc
from dataclasses import dataclass
from typing import List

from Abstract.GameObject import GameObject


@dataclass
class GameInfoBase(metaclass=abc.ABCMeta):
    max_rounds: int
    round_number: int
    game_objects: List[GameObject]
