from DungeonCrawl.DungeonCrawlUtils import count_dungeoneer_weapons
from DungeonCrawl.Model.GameObjects.Abstract.Weapon import Weapon
from DungeonCrawl.Model.GameObjects.Dungeoneer import Dungeoneer


def test_correct_weapon_count():
    dungeoneer = Dungeoneer(items=[Weapon(x_tile=1, y_tile=1, initial_x=1, initial_y=1, name="w1", owner_name="game"),
                                   Weapon(x_tile=2, y_tile=2, initial_x=2, initial_y=2, name="w2", owner_name="game")]
                            , x_tile=1, y_tile=1, initial_x=1, initial_y=1, owner_name="coco", name="cocoknight")

    result = count_dungeoneer_weapons(dungeoneer)

    assert result == 2


def test_empty_list_correct_weapon_count():
    dungeoneer = Dungeoneer(items=[]
                            , x_tile=1, y_tile=1, initial_x=1, initial_y=1, owner_name="coco", name="cocoknight")

    result = count_dungeoneer_weapons(dungeoneer)

    assert result == 0
