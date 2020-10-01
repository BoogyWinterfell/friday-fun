from typing import List, Tuple

from DungeonCrawl.Model.GameObjects.Tile import Tile


class DungeonGrid(object):
    def __init__(self, tiles: List[Tile], rows: int = 10, columns: int = 10):
        self.map = []
        for row in range(0, rows - 1):
            self.map.append([])
            for column in range(0, columns - 1):
                self.map[row].append(tiles.pop(0))

    def __getitem__(self, key: Tuple[int]):
        return self.map[key[0]][key[1]]
