from Abstract.GameInfoBase import GameInfoBase


class PlayerGameInfo(GameInfoBase):
    def __init__(self, game_info: GameInfoBase):
        super().__init__(game_info.max_rounds, game_info.round_number)
        self.game_info = game_info
