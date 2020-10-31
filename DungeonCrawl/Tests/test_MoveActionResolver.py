import copy
from typing import Tuple

from DungeonCrawl.ActionResolvers.MoveActionResolver import MoveActionResolver
from DungeonCrawl.Model.Actions.MoveAction import MoveAction
from DungeonCrawl.Tests.fixtures.fixture_DungeonCrawlGameInfo import get_default_game


def test_move_works_down():
    # Arrange
    action1 = MoveAction(name="move", caller_name="coco", moved_object_name="cocoKnight", direction="down")

    # Act & assert
    inner_test_move_works((0, 0), (0, 1), action1)


def test_move_works_up():
    # Arrange
    action1 = MoveAction(name="move", caller_name="coco", moved_object_name="cocoKnight", direction="up")

    # Act & assert
    inner_test_move_works((0, 1), (0, 0), action1)


def test_move_works_left():
    # Arrange
    action1 = MoveAction(name="move", caller_name="coco", moved_object_name="cocoKnight", direction="left")

    # Act & assert
    inner_test_move_works((0, 0), (0, 1), action1)


def test_move_works_right():
    # Arrange
    action1 = MoveAction(name="move", caller_name="coco", moved_object_name="cocoKnight", direction="right")

    # Act & assert
    inner_test_move_works((0, 0), (0, 1), action1)


def inner_test_move_works(original_tile_index: Tuple[int, int], expected_tile_index: Tuple[int, int],
                          action: MoveAction):
    # Arrange
    initial_info = get_default_game()
    initial_grid = initial_info.grid
    expected_grid = copy.deepcopy(initial_grid)
    dungeoneer_to_add = expected_grid[original_tile_index].objects_on_tile[0]
    dungeoneer_to_add.x_tile = expected_tile_index[0]
    dungeoneer_to_add.y_tile = expected_tile_index[1]
    expected_grid[expected_tile_index].objects_on_tile.append(dungeoneer_to_add)
    expected_grid[original_tile_index].objects_on_tile.clear()

    resolver = MoveActionResolver()
    # Act
    resolved_info = resolver.resolve_action(actions=[action], game_state=initial_info)
    # Assert

    assert expected_grid.tiles == resolved_info.grid.tiles
