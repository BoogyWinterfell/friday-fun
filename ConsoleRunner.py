from Abstract.Bot import Bot
from Abstract.GameRunner import GameRunner
from DungeonCrawl.DungeonCrawlGameEngine import DungeonCrawlGameEngine
from DungeonCrawl.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.DungeonCrawlPlayerGameInfo import DungeonCrawlPlayerGameInfo
from DungeonCrawl.Model.ActionResolvers.MoveActionResolver import MoveActionResolver
from DungeonCrawl.Model.GameObjects.Abstract.Treasure import Treasure
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer
from DungeonCrawl.Model.GameObjects.Tile import Tile
from DungeonCrawl.Model.WinChecks.TreasureWinCheck import TreasureWinCheck


def main():
    engine = DungeonCrawlGameEngine([MoveActionResolver()])
    info = setup_game()
    win_checks = [TreasureWinCheck(2)]
    player_info_type = DungeonCrawlPlayerGameInfo
    runner = GameRunner(engine, info, win_checks, player_info_type)
    runner.run_game()


def setup_game() -> DungeonCrawlEngineGameInfo:
    bots = {"coco": Bot(), "Jumbo": Bot()}
    p1_dungeoneer = \
        Dungeoneer(name="cocoKnight", owner_name="coco", x_tile=0, y_tile=0, initial_x=0, initial_y=0, items=[])
    bots["coco"].items.append(p1_dungeoneer)

    p2_dungeoneer = \
        Dungeoneer(name="JumboKnight", owner_name="Jumbo", x_tile=0, y_tile=0, initial_x=0, initial_y=0, items=[])
    bots["Jumbo"].items.append(p2_dungeoneer)

    t1 = Treasure(name="coin1", owner_name="game", value=1, initial_x=0, initial_y=4, x_tile=1, y_tile=1)
    t2 = Treasure(name="coin2", owner_name="game", value=1, initial_x=4, initial_y=0, x_tile=1, y_tile=1)
    w1 = Weapon(name="Weapon1", owner_name="game", initial_x=1, initial_y=1, x_tile=1, y_tile=1)
    w2 = Weapon(name="Weapon2", owner_name="game", initial_x=2, initial_y=2, x_tile=2, y_tile=2)
    w3 = Weapon(name="Weapon3", owner_name="game", initial_x=3, initial_y=3, x_tile=3, y_tile=3)
    no_walls = [False, False, False, False]
    tiles = [Tile(no_walls, [p1_dungeoneer]), Tile(no_walls), Tile(no_walls), Tile(no_walls), Tile(no_walls, [t2]),
             Tile(no_walls), Tile(no_walls, [w1]), Tile(no_walls), Tile(no_walls), Tile(no_walls),
             Tile(no_walls), Tile(no_walls), Tile(no_walls, [w2]), Tile(no_walls), Tile(no_walls),
             Tile(no_walls), Tile(no_walls), Tile(no_walls), Tile(no_walls, [w3]), Tile(no_walls),
             Tile(no_walls, [t1]), Tile(no_walls), Tile(no_walls), Tile(no_walls), Tile(no_walls, [p2_dungeoneer])]
    initial_info = DungeonCrawlEngineGameInfo(bots, tiles, rows=5, columns=5)
    return initial_info


if __name__ == "__main__":
    main()
