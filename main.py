#!/usr/bin/env python
import os
from stockfish import Stockfish
from get_all_user_games import get_user_game_archives_from_chess_dot_com
from Classes.Board import Board

archive = get_user_game_archives_from_chess_dot_com(user="checkmatejunky")
for game in archive:
    print(game["match"])
#     # find_mistakes(game)
    engine = Stockfish(path=os.environ["STOCKFISH"])
#
    engine.set_position()
    print(engine.get_board_visual())
    for move in game["match"]:
        print(move)
        print(engine.is_move_correct(move))
        engine.make_moves_from_current_position([move])
        print(engine.get_board_visual())

#     print(engine.get_best_move())
#     engine.set_position(game["match"])

