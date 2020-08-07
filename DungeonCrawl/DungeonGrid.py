from DungeonCrawl.Tile import Tile


class DungeonGrid(object):
    def __init__(self, rows: int, columns: int):
        self.map = []
        for row in range(1, rows):
            self.map.append([])
            for column in range(1, columns):
                self.map[row].append(Tile())

