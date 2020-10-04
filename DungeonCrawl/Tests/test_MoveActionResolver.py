import copy

from DungeonCrawl.ActionResolvers.MoveActionResolver import MoveActionResolver
from DungeonCrawl.Model.Actions.MoveAction import MoveAction
from DungeonCrawl.Tests.fixtures.fixture_DungeonCrawlGameInfo import get_default_game


def test_move_works():
    # Arrange
    initial_info = get_default_game()
    initial_grid = initial_info.grid
    expected_grid = copy.deepcopy(initial_grid)
    dungeoneer_to_add = expected_grid.map[0][0].objects_on_tile[0]
    dungeoneer_to_add.y_tile = 1
    expected_grid.map[0][1].objects_on_tile.append(dungeoneer_to_add)
    expected_grid.map[0][0].objects_on_tile.clear()

    action1 = MoveAction(name="move", caller_name="coco", moved_object_name="cocoKnight", direction=1)

    resolver = MoveActionResolver()
    # Act
    resolved_info = resolver.resolve_action(actions=[action1], game_state=initial_info)
    # Assert

    assert expected_grid.map == resolved_info.grid.map
