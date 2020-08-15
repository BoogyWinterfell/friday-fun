from typing import List

from DungeonCrawl.Tile import Tile


class DungeonGrid(object):
    def __init__(self, tiles: List[Tile], rows: int = 10, columns: int = 10):
        self.map = []
        for row in range(0, rows - 1):
            self.map.append([])
            for column in range(0, columns - 1):
                self.map[row].append(tiles.pop(0))

