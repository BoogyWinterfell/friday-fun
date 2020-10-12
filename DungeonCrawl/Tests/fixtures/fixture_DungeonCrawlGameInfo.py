from typing import Dict, Tuple

from DungeonCrawl.Model.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.Treasure import Treasure
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer
from DungeonCrawl.Model.GameObjects.Tile import Tile
from DungeonCrawl.Tests.fixtures.fixture_DumbBot import DumbBot


def get_default_game() -> DungeonCrawlEngineGameInfo:
    bots = [DumbBot(name="coco", items=[]), DumbBot(name="Jumbo", items=[])]
    p1_dungeoneer = \
        Dungeoneer(name="cocoKnight", owner_name="coco", x_tile=0, y_tile=0, initial_x=0, initial_y=0, items=[])
    bots[0].items.append(p1_dungeoneer)

    p2_dungeoneer = \
        Dungeoneer(name="JumboKnight", owner_name="Jumbo", x_tile=0, y_tile=0, initial_x=0, initial_y=0, items=[])
    bots[1].items.append(p2_dungeoneer)

    t1 = Treasure(name="coin1", owner_name="game", value=1, initial_x=0, initial_y=4, x_tile=1, y_tile=1)
    t2 = Treasure(name="coin2", owner_name="game", value=1, initial_x=4, initial_y=0, x_tile=1, y_tile=1)
    w1 = Weapon(name="Weapon1", owner_name="game", initial_x=1, initial_y=1, x_tile=1, y_tile=1)
    w2 = Weapon(name="Weapon2", owner_name="game", initial_x=2, initial_y=2, x_tile=2, y_tile=2)
    w3 = Weapon(name="Weapon3", owner_name="game", initial_x=3, initial_y=3, x_tile=3, y_tile=3)
    no_walls = [False, False, False, False]

    tiles: Dict[Tuple[int, int], Tile] = {(0, 0): Tile(*no_walls, objects_on_tile=[p1_dungeoneer]),
                                          (0, 1): Tile(*no_walls, objects_on_tile=[]),
                                          (0, 2): Tile(*no_walls, objects_on_tile=[]),
                                          (0, 3): Tile(*no_walls, objects_on_tile=[]),
                                          (0, 4): Tile(*no_walls, objects_on_tile=[t2]),
                                          (1, 0): Tile(*no_walls, objects_on_tile=[]),
                                          (1, 1): Tile(*no_walls, objects_on_tile=[w1]),
                                          (1, 2): Tile(*no_walls, objects_on_tile=[]),
                                          (1, 3): Tile(*no_walls, objects_on_tile=[]),
                                          (1, 4): Tile(*no_walls, objects_on_tile=[]),
                                          (2, 0): Tile(*no_walls, objects_on_tile=[]),
                                          (2, 1): Tile(*no_walls, objects_on_tile=[]),
                                          (2, 2): Tile(*no_walls, objects_on_tile=[w2]),
                                          (2, 3): Tile(*no_walls, objects_on_tile=[]),
                                          (2, 4): Tile(*no_walls, objects_on_tile=[]),
                                          (3, 0): Tile(*no_walls, objects_on_tile=[]),
                                          (3, 1): Tile(*no_walls, objects_on_tile=[]),
                                          (3, 2): Tile(*no_walls, objects_on_tile=[]),
                                          (3, 3): Tile(*no_walls, objects_on_tile=[w3]),
                                          (3, 4): Tile(*no_walls, objects_on_tile=[]),
                                          (4, 0): Tile(*no_walls, objects_on_tile=[t1]),
                                          (4, 1): Tile(*no_walls, objects_on_tile=[]),
                                          (4, 2): Tile(*no_walls, objects_on_tile=[]),
                                          (4, 3): Tile(*no_walls, objects_on_tile=[]),
                                          (4, 4): Tile(*no_walls, objects_on_tile=[p2_dungeoneer])}

    grid = DungeonGrid(tiles, rows=5, columns=5)
    initial_info = DungeonCrawlEngineGameInfo(max_rounds=500, round_number=0, players=bots, grid=grid, respawn_time=20)
    return initial_info
