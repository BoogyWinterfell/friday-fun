from typing import List, Tuple

from DungeonCrawl.Model.GameObjects.Tile import Tile


class DungeonGrid(object):
    def __init__(self, tiles: List[Tile], rows: int = 10, columns: int = 10):
        self.map: List[List[Tile]] = []
        for row in range(0, rows):
            self.map.append([])
            for column in range(0, columns):
                self.map[row].append(tiles.pop(0))
