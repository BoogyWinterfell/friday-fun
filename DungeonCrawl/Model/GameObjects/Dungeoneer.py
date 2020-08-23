from typing import List

from DungeonCrawl.Model.GameObjects.Abstract.GameObject import GameObject
from DungeonCrawl.Model.GameObjects.Treasure import Treasure
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon


class Dungeoneer(GameObject):
    weapons: List[Weapon]
    treasure: List[Treasure]
