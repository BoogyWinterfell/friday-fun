from typing import List

from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.GameInfo import GameInfo


class GameRunner:
    def __init__(self, engine: GameEngine, initial_state: GameInfo):
        self._round_number = 0
        self.engine = engine
        self.initial_state = initial_state
        self.game_log = [self.initial_state]

# TODO: Win check
    def run_game(self) -> List[GameInfo]:
        for i in range(0, self.game_log[0].max_rounds):
            self.game_log.append(self.run_round())

        return self.game_log

    def run_round(self) -> GameInfo:
        player_inputs = []
        current_state = self.game_log[self._round_number]
        for name, player in current_state.players.items():
            # TODO: exception handling
            player_inputs.append(player.play_round(current_state))

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
