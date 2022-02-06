from .History import History

class Position:
    def __init__(self, state):
        self.state: tuple = (turn, color)


    def is_players_turn(self) -> bool:
        return True

    def is_check(self) -> bool:
        return True

    def is_checkmate(self) -> bool:
        return True
