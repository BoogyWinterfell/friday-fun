import abc
from dataclasses import dataclass


@dataclass
class GameInfoBase(metaclass=abc.ABCMeta):
    max_rounds: int
    round_number: int
