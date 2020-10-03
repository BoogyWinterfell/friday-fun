from dataclasses import dataclass

from Abstract.NamedObject import NamedObject


@dataclass
class GameAction(NamedObject):
    caller_name: str
