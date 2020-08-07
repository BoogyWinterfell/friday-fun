
class GameInfo:
    def __init__(self, players, round_number=0):
        self.players = players
        self.round_number = round_number

    def get_round_number(self):
        return self._round_number

