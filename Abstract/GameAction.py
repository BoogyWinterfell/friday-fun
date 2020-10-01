from dataclasses import dataclass


@dataclass
class GameAction:
    name: str
    caller_name: str
