#!/usr/bin/env python
import os
import asyncio
import re
from stockfish import Stockfish
from get_all_user_games import get_user_game_archives_from_chess_dot_com
import chess
archive = get_user_game_archives_from_chess_dot_com(user="checkmatejunky")

# def analyze_position():
#     info = engine.analyse(board, chess.engine.Limit(time=0.1))
#     print(info["score"])
#
#
# def parse_game():
#     analyze_position()
#
#
# for game in archive:
#     print(game["match"])
# #     # find_mistakes(game)
#     g = chess.pgn.Game()
#     board = chess.Board()

async def main() -> None:
    transport, engine = await chess.engine.popen_uci(os.environ["STOCKFISH"])

    board = chess.Board()

    worst_move = {
        "score_delta": 0,
        "move": 0

    }

    while not board.is_game_over():
        print("\n", board.fullmove_number)
        print(board)
        result = await engine.play(board, chess.engine.Limit(time=1), info=chess.engine.Info.ALL)
        print(re.search(r'[\+-]{0,1}\d+', str(result.info["score"])).group(0))
        info = await engine.analyse(board, chess.engine.Limit(time=0.1))
        print(info["score"])
        info = await engine.analyse(board, chess.engine.Limit(time=0.1))
        print(info["score"])
        info = await engine.analyse(board, chess.engine.Limit(time=0.1))
        print(info["score"])
        prev_move_score = -int(re.search(r'[\+-]{0,1}\d+', str(result.info["score"])).group(0))
        board.push(result.move)
        result = await engine.play(board, chess.engine.Limit(time=1), info=chess.engine.Info.ALL)
        curr_score = int(re.search(r'[\+-]{0,1}\d+', str(result.info["score"])).group(0))
        delta = curr_score - prev_move_score
        print(prev_move_score, curr_score, delta)
        if board.turn == chess.WHITE:
            if worst_move["score_delta"] < delta and board.turn:
                worst_move["score_delta"] = delta
                worst_move["move"] = board.fullmove_number

    print(board.is_checkmate())
    print(board.is_fifty_moves())
    print(worst_move["score_delta"], worst_move["move"])
    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())

#     node = g.add_variation(chess.Move.from_uci("e2e4"))
#
#     asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
#     asyncio.run(parse_game())


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


