from typing import Dict

from Abstract.Bot import Bot


class GameInfo:
    def __init__(self, players: Dict[str, Bot], max_rounds=1000):
        self.players = players
        self.round_number = 0
        self.max_rounds = max_rounds
