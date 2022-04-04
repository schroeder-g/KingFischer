#!/usr/bin/env python
import os
import asyncio
from stockfish import Stockfish
from get_all_user_games import get_user_game_archives_from_chess_dot_com
import chess
archive = get_user_game_archives_from_chess_dot_com(user="checkmatejunky")

async def analyze_position():
    info = await engine.analyse(board, chess.engine.Limit(time=0.1))
    print(info["score"])


async def parse_game():
    await analyze_position()


for game in archive:
    print(game["match"])
#     # find_mistakes(game)
    g = chess.pgn.Game()
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci(
        os.environ["STOCKFISH"])
    node = g.add_variation(chess.Move.from_uci("e2e4"))

    asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
    asyncio.run(parse_game())


    # stockfish = Stockfish(path=os.environ["STOCKFISH"], parameters={"Minimum Thinking Time": 200})

#
    # stockfish.set_position()
    # print(stockfish.get_board_visual())
    # for move in game["match"]:
    #     print(stockfish.get_best_move(), move)
    #     print(stockfish.get_best_move() == move)
    #     eval1 = stockfish.get_evaluation()
    #     stockfish.make_moves_from_current_position([move])
    #     eval2 = stockfish.get_evaluation()
    #     print(stockfish.get_evaluation())
    #     print(stockfish.get_evaluation())
    #     print(eval1, eval2, game["player_color"])
    #     info = engine.analyse(board, chess.engine.Limit(depth=20))
    #     print("Score:", info["score"])
    #     print(stockfish.get_board_visual())
    #
    #     evaluation = engine.go(movetime=5000)
        # print('best move: ', board.san(evaluation[0]))

#     print(engine.get_best_move())
#     engine.set_position(game["match"])


