from typing import Type

from DungeonCrawl.Model.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.Model.DungeonCrawlPlayerGameInfo import DungeonCrawlPlayerGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.Treasure import Treasure
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


def count_dungeoneer_weapons(dungeoneer: Dungeoneer):
    return len(get_dungeoneer_items_by_type(dungeoneer, Weapon))


def get_dungeoneer_items_by_type(dungeoneer: Dungeoneer, item_type: Type):
    return [w for w in dungeoneer.items if isinstance(w, item_type)]


def get_dungeoneer_treasure_worth(dungeoneer: Dungeoneer):
    return sum([t.value for t in get_dungeoneer_items_by_type(dungeoneer, Treasure) if isinstance(t, Treasure)])


def player_info_from_engine_game_info(info: DungeonCrawlEngineGameInfo):
    return DungeonCrawlPlayerGameInfo(info.max_rounds, info.round_number, info.respawn_time, info.grid)
