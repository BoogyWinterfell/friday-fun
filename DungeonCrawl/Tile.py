from typing import List


class Tile(object):
    def __init__(self, walls_config: List[bool], objects_on_tile: List = None):
        if objects_on_tile is None:
            objects_on_tile = []
        self.left_wall = walls_config[0]
        self.top_wall = walls_config[1]
        self.right_wall = walls_config[2]
        self.bottom_wall = walls_config[3]
        self.objects_on_tile = objects_on_tile
