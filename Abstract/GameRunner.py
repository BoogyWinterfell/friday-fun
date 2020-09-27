from typing import List, Type, Dict

from Abstract.GameAction import GameAction
from Abstract.GameEngine import GameEngine
from Abstract.EngineGameInfo import EngineGameInfo
from Abstract.WinCheck import WinCheck


class GameRunner:
    def __init__(self, engine: GameEngine, initial_state: EngineGameInfo, win_checkers: List[WinCheck],
                 player_info_type: Type):
        self._round_number = 0
        self.engine = engine
        self.initial_state = initial_state
        self.game_log = [self.initial_state]
        self.win_checkers = win_checkers
        self.player_info_type = player_info_type

    def run_game(self) -> List[EngineGameInfo]:
        for i in range(0, self.game_log[0].max_rounds):
            for check in self.win_checkers:
                if check.search_for_winners(self.game_log[i]):
                    # TODO: There are winners, Report it!!!
                    print(str(check.search_for_winners(self.game_log[i])) + " Won!!!")
                    return self.game_log

            self.game_log.append(self.run_round())

        return self.game_log

    def run_round(self) -> EngineGameInfo:
        player_inputs = {}
        current_state = self.game_log[self._round_number]
        for name, player in current_state.players.items():
            # TODO: exception handling
            # Look here I'm using the type from before to instantiate the proper info type.
            player_inputs[name] = player.play_round(self.player_info_type(current_state))

        new_game_state = self.read_player_inputs(player_inputs)

        self._round_number += 1
        new_game_state.round_number = self._round_number

        self.game_log.append(new_game_state)
        return new_game_state

    def read_player_inputs(self, player_inputs: Dict[str, List[GameAction]]) -> EngineGameInfo:
        game_state = self.game_log[self._round_number]
        game_state_copy = EngineGameInfo(game_state.players, game_state.round_number)

        self.engine.resolve_actions(player_inputs, game_state_copy)

        return game_state_copy
