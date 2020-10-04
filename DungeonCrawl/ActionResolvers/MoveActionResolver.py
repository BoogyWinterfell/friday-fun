from typing import List

from Abstract.ActionResolver import ActionResolver
from Abstract.EngineGameInfo import EngineGameInfo
from Abstract.GameAction import GameAction
from DungeonCrawl.DungeonCrawlUtils import count_dungeoneer_weapons, get_dungeoneer_items_by_type
from DungeonCrawl.Model.Actions.MoveAction import MoveAction
from DungeonCrawl.Model.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


class MoveActionResolver(ActionResolver):
    def __init__(self):
        self.direction_resolve_dict = {1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)}

    def resolve_action(self, actions: List[GameAction], game_state: EngineGameInfo) -> EngineGameInfo:
        info = DungeonCrawlEngineGameInfo(**game_state.__dict__)
        for action in [action for action in actions if type(action) == MoveAction]:
            move = MoveAction(**action.__dict__)
            self.move_entity(move, info)

        new_game_state = self.resolve_collisions(info)
        return new_game_state

    def move_entity(self, action: MoveAction, game_state: DungeonCrawlEngineGameInfo):
        player = [p for p in game_state.players if p.name == action.caller_name]
        if len(player) != 1:
            raise Exception("There were" + str(len(player)) + "players instead of 1.")

        moving_items = [item for item in player[0].items if item.name == action.moved_object_name]
        if len(moving_items) > 1:
            raise Exception("There were at least two items with the same name.")

        moving_item = moving_items[0]
        if moving_item:
            x_move, y_move = self.direction_resolve_dict[action.direction]
            current_x = moving_item.x_tile
            current_y = moving_item.y_tile
            self.move_object_between_tiles(game_state, moving_item, current_x, current_y, current_x + x_move,
                                           current_y + y_move)

    def resolve_collisions(self, game_state: DungeonCrawlEngineGameInfo) -> EngineGameInfo:
        players_items = [player.items for player in game_state.players]
        dungeoneers = []
        for items in players_items:
            for item in items:
                if isinstance(item, Dungeoneer):
                    dungeoneers.append(item)

        for row in game_state.grid.map:
            for tile in row:
                # Will be changed to all hostiles and dungeoneers later.
                dungeoneers = [x for x in tile.objects_on_tile if isinstance(x, Dungeoneer)]
                if len(dungeoneers) < 2:
                    continue
                weapons_count = [count_dungeoneer_weapons(d) for d in dungeoneers]
                max_weapons = max(weapons_count)
                fight_winners = [d for d in dungeoneers if count_dungeoneer_weapons(d) == max_weapons]
                fight_losers = [d for d in dungeoneers if count_dungeoneer_weapons(d) < max_weapons]
                self.update_losers(fight_losers, game_state)

                max_weapon_losers = max([count_dungeoneer_weapons(d) for d in fight_losers])
                self.update_winners(fight_winners, game_state, max_weapon_losers)

        return game_state

    def update_winners(self, fight_winners, game_state, max_weapon_losers):
        for winner in fight_winners:
            weapons = get_dungeoneer_items_by_type(winner, Weapon)
            weapons_count = count_dungeoneer_weapons(winner)
            for i in range(0, min([max_weapon_losers, weapons_count])):
                weapon = winner.items.remove(weapons[len(weapons - 1)])
                self.move_object_to_tile(game_state, weapon, weapon.initial_x, weapon.initial_y)

    def update_losers(self, fight_losers, game_state):
        for loser in fight_losers:
            for item in loser.items:
                self.move_object_to_tile(game_state, item, item.initial_x, item.initial_y)
            loser.items.clear()

            self.move_object_between_tiles(game_state, loser, loser.x_tile,
                                           loser.y_tile, loser.initial_y, loser.initial_x)

    # TODO: Consider moving these functions to utilities, Reconsider entire Pure Data Design Decision.

    def move_object_between_tiles(self, game_state: DungeonCrawlEngineGameInfo, object_to_move: DungeonCrawlGameObject,
                                  current_x: int, current_y: int, x, y):
        game_state.grid.map[current_x][current_y].objects_on_tile.remove(object_to_move)
        self.move_object_to_tile(game_state, object_to_move, x, y)

    def move_object_to_tile(self, game_state: DungeonCrawlEngineGameInfo, object_to_move: DungeonCrawlGameObject, x, y):
        object_to_move.x_tile = x
        object_to_move.y_tile = y
        game_state.grid.map[x][y].objects_on_tile.append(object_to_move)
