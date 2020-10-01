from dataclasses import dataclass

from DungeonCrawl.Model.GameObjects.Abstract.Item import Item


@dataclass
class Treasure(Item):
    value: int
