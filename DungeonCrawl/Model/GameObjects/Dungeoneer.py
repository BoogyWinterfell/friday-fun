from typing import List

from DungeonCrawl.Model.GameObjects.Abstract.GameObject import GameObject
from DungeonCrawl.Model.GameObjects.Abstract.Item import Item


class Dungeoneer(GameObject):
    items: List[Item]
