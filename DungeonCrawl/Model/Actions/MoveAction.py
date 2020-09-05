from Abstract.GameAction import GameAction


class MoveAction(GameAction):
    moved_object_name: str
    direction: int
