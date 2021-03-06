from typing import List

from Abstract.ActionResolver import ActionResolver
from Abstract.GameAction import GameAction
from Abstract.EngineGameInfo import EngineGameInfo
from DungeonCrawl.DungeonCrawlEngineGameInfo import DungeonCrawlEngineGameInfo
from DungeonCrawl.DungeonCrawlUtils import count_dungeoneer_weapons, get_dungeoneer_items_by_type
from DungeonCrawl.Model.Actions.MoveAction import MoveAction
from DungeonCrawl.Model.GameObjects.Abstract.DungeonCrawlGameObject import DungeonCrawlGameObject
from DungeonCrawl.Model.GameObjects.Abstract.Item import Item
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


class MoveActionResolver(ActionResolver):
    def __init__(self):
        self.resolve_dict = {1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)}

    def resolve_action(self, actions: List[GameAction], game_state: EngineGameInfo) -> EngineGameInfo:
        info = DungeonCrawlEngineGameInfo(**game_state.__dict__)
        for action in [action for action in actions if type(action) == MoveAction]:
            move = MoveAction(**action.__dict__)
            self.move_entity(move, info)

        new_game_state = self.resolve_collisions(info)
        return new_game_state

    def move_entity(self, action: MoveAction, game_state: DungeonCrawlEngineGameInfo):
        player = game_state.players[action['caller_name']]

        moving_items = [item for item in player.items if item['name'] == action['moved_object_name']]
        if len(moving_items) > 1:
            raise Exception("There were at least two items with the same name.")

        moving_item = moving_items[0]
        if moving_item:
            x_move, y_move = self.resolve_dict[action['direction']]
            current_x = moving_item['x_tile']
            current_y = moving_item['y_tile']
            self.move_to_tile(game_state, moving_item, current_x, current_y, current_x + x_move,
                              current_y + y_move)

    def resolve_collisions(self, game_state: DungeonCrawlEngineGameInfo) -> EngineGameInfo:
        for row in game_state.grid:
            for tile in row:
                for tile_object in tile:
                    dungeoneers = [x for x in tile.objects_on_tile if isinstance(x, Dungeoneer)]
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
                weapon = winner['items'].pop(weapons[len(weapons - 1)])
                self.move_item_back(game_state, weapon, weapon['initial_x'], weapon['initial_y'])

    def update_losers(self, fight_losers, game_state):
        for loser in fight_losers:
            for item in loser['items']:
                self.move_item_back(game_state, item, item['initial_x'], item['initial_y'])

            self.move_to_tile(game_state, loser, loser['x_tile'],
                              loser['y_tile'], loser['initial_y'], loser['initial_x'])

    # TODO: Consider moving these functions to utilities, Reconsider entire Pure Data Design Decision.
    def move_to_tile(self, game_state: DungeonCrawlEngineGameInfo, object_to_move: DungeonCrawlGameObject, current_x, current_y, x, y):
        game_state.grid[current_x][current_y].objects_on_tile.pop(object_to_move)
        object_to_move['x_tile'] = x
        object_to_move['y_tile'] = y
        game_state.grid[x][y].objects_on_tile.add(object_to_move)

    def move_item_back(self, game_state: DungeonCrawlEngineGameInfo, object_to_move: Item, x, y):
        object_to_move['x_tile'] = x
        object_to_move['y_tile'] = y
        game_state.grid[x][y].objects_on_tile.add(object_to_move)
