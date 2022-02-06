from stockfish import Stockfish
from datetime import datetime
from .Position import Position

class History:
    def __init__(self):
        self.main_line: list[Position]
        self.possible_lines # Add the capability to explore multiple lines
