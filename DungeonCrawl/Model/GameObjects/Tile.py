from dataclasses import dataclass

from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject


@dataclass
class Tile(DungeonCrawlGameObject):
    left_wall: bool
    top_wall: bool
    right_wall: bool
    bottom_wall: bool
