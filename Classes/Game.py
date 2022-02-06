from stockfish import Stockfish
from datetime import datetime
import os


class Game:
    def __init__(self, match, player_color, opening, result, state=(0,0)):
        self.match: list[list[str]] = match
        self.player_color: str = player_color
        self.opening: str = opening
        self.result:  str = result
        self.current_position: Position = state
        self.engine: Stockfish = Stockfish(path="")
        #self.date: Date = ...

    def set_position(self, turn, color):
        self.current_position = Position((turn, color), self.match[turn])

    def print_board(self):
        print(Stockfish.get_board_visual())

    def get_best_move(self):
        return self.current_position

    def get_stockfish_position(self) -> str:
        print(engine)

    def initialize_interactive_game(self, game: Game):
        print("not mistaken\n", game)

    def get_history(self) -> History:
        return true
        # return History(position)
