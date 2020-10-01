from dataclasses import dataclass
from typing import List

from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject


@dataclass
class Tile(object):
    left_wall: bool
    top_wall: bool
    right_wall: bool
    bottom_wall: bool
    objects_on_tile: List[DungeonCrawlGameObject]
