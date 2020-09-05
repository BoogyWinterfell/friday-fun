from typing import TypedDict


class GameObject(TypedDict):
    name: str
    owner_name: str
    x_tile: int
    y_tile: int
    initial_x: int
    initial_y: int
