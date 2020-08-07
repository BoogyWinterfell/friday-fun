import abc
from typing import Tuple

from Abstract.Bot import Bot
from Abstract.GameAction import GameAction
from Abstract.GameInfo import GameInfo


class Game(metaclass=abc.ABCMeta):
    def __init__(self, players: Tuple[Bot], initial_state: GameInfo):
        self.players = players
        self._round_number = 0
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

    def read_player_inputs(self, player_inputs) -> GameInfo:
        game_state = self.game_log[self._round_number]
        game_state_copy = GameInfo(game_state.players, game_state.get_round_number())

        for actions in zip(*player_inputs):
            self.resolve_actions(actions, game_state_copy)

        return game_state_copy

    @abc.abstractmethod
    def resolve_actions(self, actions: Tuple[GameAction], game_state: GameInfo):
        pass
