#!/usr/bin/env python
import os
from stockfish import Stockfish
from get_all_user_games import get_user_game_archives_from_chess_dot_com
from Classes.Board import Board

# archive = get_user_game_archives_from_chess_dot_com(user="checkmatejunky")
# for game in archive:
#     engine = Stockfish(path=os.environ["STOCKFISH"])
#     print(game["match"])
#     # find_mistakes(game)
#
#     engine.set_position(["e2e4", "d7d5", "e4d5"])
#     print(engine.get_board_visual())
#     print(engine.get_best_move())
#     engine.set_position(game["match"])

