from dataclasses import dataclass

from Abstract.GameAction import GameAction


@dataclass
class MoveAction(GameAction):
    moved_object_name: str
    direction: int
