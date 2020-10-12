from typing import List, Tuple

from DungeonCrawl.Model.GameObjects.Tile import Tile


class DungeonGrid(object):
    def __init__(self, tiles: List[Tile], rows: int, columns: int):
        self.tiles: List[Tile] = tiles
        self.rows = rows
        self.columns = columns

    def __getitem__(self, pos: Tuple[int, int]):
        row, column = pos
        return self.tiles[(self.rows * row) + column]
