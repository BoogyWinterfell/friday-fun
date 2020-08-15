from typing import Tuple, List

from Abstract.Bot import Bot
from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.GameInfo import GameInfo


class GameRunner:
    def __init__(self, engine: GameEngine, players: Tuple[Bot], initial_state: GameInfo):
        self.players = players
        self._round_number = 0
        self.engine = engine
        initial_state.players = players
        self.game_log = [initial_state]

    def run_round(self) -> GameInfo:
        player_inputs = []

        for player in self.players:
            player_inputs.append(player.play_round(self.game_log[self._round_number]))

        new_game_state = self.read_player_inputs(player_inputs)

        self._round_number += 1
        new_game_state.round_number = self._round_number

        self.game_log.append(new_game_state)
        return new_game_state

    def read_player_inputs(self, player_inputs: List[List[GameAction]]) -> GameInfo:
        game_state = self.game_log[self._round_number]
        game_state_copy = GameInfo(game_state.players, game_state.round_number)

        self.engine.resolve_actions(player_inputs, game_state_copy)

        return game_state_copy
