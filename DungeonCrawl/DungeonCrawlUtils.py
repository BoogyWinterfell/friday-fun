from typing import Type, List

from DungeonCrawl.Model.DungeonCrawlGameInfo import DungeonCrawlGameInfo
from DungeonCrawl.Model.DungeonCrawlPlayerGameInfo import DungeonCrawlPlayerGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject
from DungeonCrawl.Model.GameObjects.Abstract.Treasure import Treasure
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer
from DungeonCrawl.Model.GameObjects.Tile import Tile


def count_dungeoneer_weapons(dungeoneer: Dungeoneer):
    return len(get_dungeoneer_items_by_type(dungeoneer, Weapon))


def get_dungeoneer_items_by_type(dungeoneer: Dungeoneer, item_type: Type):
    return [w for w in dungeoneer.items if isinstance(w, item_type)]


def get_dungeoneer_treasure_worth(dungeoneer: Dungeoneer):
    return sum([t.value for t in get_dungeoneer_items_by_type(dungeoneer, Treasure) if isinstance(t, Treasure)])


def player_info_from_engine_game_info(info: DungeonCrawlGameInfo):
    return DungeonCrawlPlayerGameInfo(info.max_rounds, info.round_number, info.respawn_time, info.grid)


def get_objects_on_tile(info: DungeonCrawlGameInfo, tile: Tile):
    x, y = tile.initial_x, tile.initial_y
    return [item for item in get_all_objects(info) if item.x_tile == x and item.y_tile == y]


def get_all_objects(info: DungeonCrawlGameInfo) -> List[DungeonCrawlGameObject]:
    objects = []
    [objects.extend(items) for items in [player.items for player in info.players]]
    return objects
