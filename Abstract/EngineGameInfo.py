from typing import Dict

from Abstract.Bot import Bot
from Abstract.GameInfoBase import GameInfoBase


class EngineGameInfo(GameInfoBase):
    def __init__(self, players: Dict[str, Bot], max_rounds: int, round_number: int):
        super().__init__(max_rounds, round_number)
        self.players = players
