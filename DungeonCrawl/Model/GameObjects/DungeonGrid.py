from typing import List, Tuple, Dict

from DungeonCrawl.Model.GameObjects.Tile import Tile


class DungeonGrid(object):
    def __init__(self, tiles: Dict[Tuple[int, int], Tile], rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.tiles: Dict[Tuple[int, int], Tile] = tiles

    def __getitem__(self, position: Tuple[int, int]):
        return self.tiles[position]
