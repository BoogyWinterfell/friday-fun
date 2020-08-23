from typing import List

from DungeonCrawl.Model.GameObjects.Abstract.Entity import Entity
from DungeonCrawl.Model.GameObjects.Abstract.Item import Item


class Dungeoneer(Entity):
    items: List[Item]
