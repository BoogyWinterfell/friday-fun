from typing import List

from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject
from DungeonCrawl.Model.GameObjects.Abstract.Item import Item


class Dungeoneer(DungeonCrawlGameObject):
    items: List[Item]
