from dataclasses import dataclass

from Abstract.GameObject import GameObject


@dataclass
class DungeonCrawlGameObject(GameObject):
    x_tile: int
    y_tile: int
    initial_x: int
    initial_y: int
