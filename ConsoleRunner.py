from Abstract.GameRunner import GameRunner
from DungeonCrawl import DungeonCrawlUtils
from DungeonCrawl.ActionResolvers.MoveActionResolver import MoveActionResolver
from DungeonCrawl.Model.DungeonCrawlGameInfo import DungeonCrawlGameInfo
from DungeonCrawl.Model.DungeonCrawlGameEngine import DungeonCrawlGameEngine
from DungeonCrawl.Tests.fixtures.fixture_DungeonCrawlGameInfo import get_default_game
from DungeonCrawl.WinChecks.TreasureWinCheck import TreasureWinCheck


def main():
    engine = DungeonCrawlGameEngine([MoveActionResolver()])
    info = get_default_game()
    win_checks = [TreasureWinCheck(2)]
    runner = GameRunner(engine, info, win_checks, DungeonCrawlUtils.player_info_from_engine_game_info, info.players)
    log = runner.run_game()
    for info in log:
        converted_info = DungeonCrawlGameInfo(**info.__dict__)
        print(converted_info)


if __name__ == "__main__":
    main()
