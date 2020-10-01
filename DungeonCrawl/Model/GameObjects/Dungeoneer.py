from dataclasses import dataclass
from typing import List

from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject
from DungeonCrawl.Model.GameObjects.Abstract.Item import Item


@dataclass
class Dungeoneer(DungeonCrawlGameObject):
    items: List[Item]
