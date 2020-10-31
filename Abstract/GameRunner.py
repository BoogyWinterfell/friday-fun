import copy
from typing import List, Dict, Callable

from Abstract.Bot import Bot
from Abstract.GameInfo import GameInfo
from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.WinCheck import WinCheck


class GameRunner:
    def __init__(self, engine: GameEngine, initial_state: GameInfo, win_checkers: List[WinCheck],
                 info_conversion: Callable, players: List[Bot]):
        self._round_number = 0
        self.engine = engine
        self.initial_state = initial_state
        self.game_log = [self.initial_state]
        self.win_checkers = win_checkers
        # This attribute is used for instantiating the proper PlayerGameInfo type of the current game.
        self.info_conversion = info_conversion
        self.players = players

    def run_game(self) -> List[GameInfo]:
        for i in range(0, self.game_log[0].max_rounds):
            for check in self.win_checkers:
                if check.search_for_winners(self.game_log[i]):
                    # TODO: There are winners, Report it!!!
                    print(str(check.search_for_winners(self.game_log[i])) + " Won!!!")
                    return self.game_log

            self.game_log.append(self.run_round())

        return self.game_log

    def run_round(self) -> GameInfo:
        player_inputs = {}
        current_state = self.game_log[self._round_number]
        for player in self.players:
            # TODO: exception handling
            # Look here I'm using the type from before to instantiate the proper info type.
            player_inputs[player.name] = player.play_round(self.info_conversion(current_state))

        new_game_state = self.read_player_inputs(player_inputs)

        self._round_number += 1
        new_game_state.round_number = self._round_number

        return new_game_state

    def read_player_inputs(self, player_inputs: Dict[str, List[GameAction]]) -> GameInfo:
        game_state_copy = copy.deepcopy(self.game_log[self._round_number])
        self.engine.resolve_actions(player_inputs, game_state_copy)
        return game_state_copy
