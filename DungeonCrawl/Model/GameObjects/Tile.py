from dataclasses import dataclass


@dataclass
class Tile:
    left_wall: bool
    top_wall: bool
    right_wall: bool
    bottom_wall: bool
