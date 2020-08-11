from typing import Tuple

from Abstract.Bot import Bot
from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo
from Abstract.Game import Game


class DungeonCrawlGame(Game):
    def __init__(self, players: Tuple[Bot], initial_state: GameInfo):
        super().__init__(players, initial_state)

    def read_player_inputs(self, player_inputs) -> GameInfo:
        game_state = self.game_log[self._round_number]
        game_state_copy = GameInfo(game_state.players, game_state.get_round_number())

        for actions in zip(*player_inputs):
            self.resolve_actions(actions, game_state_copy)

        return game_state_copy

    def resolve_actions(self, actions: Tuple[GameAction], game_state: GameInfo):
        pass
