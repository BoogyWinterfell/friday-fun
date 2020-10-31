from typing import Dict, Tuple

from DungeonCrawl.Model.DungeonCrawlBotInfo import DungeonCrawlBotInfo
from DungeonCrawl.Model.DungeonCrawlGameInfo import DungeonCrawlGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.Treasure import Treasure
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.DungeonGrid import DungeonGrid
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer
from DungeonCrawl.Model.GameObjects.Tile import Tile
from DungeonCrawl.Tests.fixtures.fixture_DumbBot import DumbBot


def get_default_game() -> DungeonCrawlGameInfo:
    game_objects = []
    p1_dungeoneer = \
        Dungeoneer(name="cocoKnight", owner_name="coco", x_tile=0, y_tile=0, initial_x=0, initial_y=0, items=[])
    game_objects.append(p1_dungeoneer)

    p2_dungeoneer = \
        Dungeoneer(name="JumboKnight", owner_name="Jumbo", x_tile=4, y_tile=4, initial_x=4, initial_y=4, items=[])
    game_objects.append(p2_dungeoneer)

    bots = [DumbBot(name="coco", info=DungeonCrawlBotInfo(items=[p1_dungeoneer])),
            DumbBot(name="Jumbo", info=DungeonCrawlBotInfo(items=[p2_dungeoneer]))]

    t1 = Treasure(name="coin1", owner_name="game", value=1, initial_x=0, initial_y=4, x_tile=1, y_tile=1)
    t2 = Treasure(name="coin2", owner_name="game", value=1, initial_x=4, initial_y=0, x_tile=1, y_tile=1)
    w1 = Weapon(name="Weapon1", owner_name="game", initial_x=1, initial_y=1, x_tile=1, y_tile=1)
    w2 = Weapon(name="Weapon2", owner_name="game", initial_x=2, initial_y=2, x_tile=2, y_tile=2)
    w3 = Weapon(name="Weapon3", owner_name="game", initial_x=3, initial_y=3, x_tile=3, y_tile=3)
    game_objects.append(t1)
    game_objects.append(t2)
    game_objects.append(w1)
    game_objects.append(w2)
    game_objects.append(w3)
    no_walls = [False, False, False, False]

    tiles: Dict[Tuple[int, int], Tile] = {(0, 0): Tile(*no_walls),
                                          (0, 1): Tile(*no_walls),
                                          (0, 2): Tile(*no_walls),
                                          (0, 3): Tile(*no_walls),
                                          (0, 4): Tile(*no_walls),
                                          (1, 0): Tile(*no_walls),
                                          (1, 1): Tile(*no_walls),
                                          (1, 2): Tile(*no_walls),
                                          (1, 3): Tile(*no_walls),
                                          (1, 4): Tile(*no_walls),
                                          (2, 0): Tile(*no_walls),
                                          (2, 1): Tile(*no_walls),
                                          (2, 2): Tile(*no_walls),
                                          (2, 3): Tile(*no_walls),
                                          (2, 4): Tile(*no_walls),
                                          (3, 0): Tile(*no_walls),
                                          (3, 1): Tile(*no_walls),
                                          (3, 2): Tile(*no_walls),
                                          (3, 3): Tile(*no_walls),
                                          (3, 4): Tile(*no_walls),
                                          (4, 0): Tile(*no_walls),
                                          (4, 1): Tile(*no_walls),
                                          (4, 2): Tile(*no_walls),
                                          (4, 3): Tile(*no_walls),
                                          (4, 4): Tile(*no_walls)}

    grid = DungeonGrid(tiles, rows=5, columns=5)
    initial_info = DungeonCrawlGameInfo(max_rounds=500, round_number=0, players=bots, grid=grid, respawn_time=20,
                                        game_objects=game_objects)
    return initial_info
