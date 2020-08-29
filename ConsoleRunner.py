from plistlib import Dict

from Abstract.Bot import Bot
from Abstract.GameInfo import GameInfo
from Abstract.GameRunner import GameRunner
from DungeonCrawl.DungeonCrawlGameEngine import DungeonCrawlGameEngine


def main():
    engine = DungeonCrawlGameEngine()
    info = get_initial_game_state()
    runner = GameRunner(engine, info)


def register_bots() -> Dict[str, Bot]:
    pass


def get_initial_game_state() -> GameInfo:
    pass


if __name__ == "__main__":
    main()
