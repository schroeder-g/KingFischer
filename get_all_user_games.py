#!/usr/bin/env python
import re
import requests
import json
import io
import chess.pgn

def get_user_game_archives_from_chess_dot_com(user: str):

    games = []
    headers = {
        'Content-type': 'application/json',
    }
    archives = json.loads(requests
                          .get(f'https://api.chess.com/pub/player/{user}/games/archives', headers=headers)
                          .content.decode('UTF-8'))["archives"]
    most_recent_month = json.loads(requests.get(archives[-1], headers=headers).content.decode('UTF-8'))
    most_recent_dirty_game = most_recent_month["games"][-1]

    cleaned_game = clean_game(most_recent_dirty_game["pgn"], user)
    return [cleaned_game]

    # Collects the entirety of a users game history
    # for url in range(len(archives)):
    #     month_of_games = json.loads(requests
    #                                 .get(archives[url], headers=headers)
    #                                 .content.decode('UTF-8'))
    #     for game in range(len(month_of_games)):
    #         games.append(clean_game(game))
    #return games


def clean_game(game: str, user):
    player_color = game[game.index(user) - 7: game.index(user) - 2]

    pgn = re.sub(r'\{.*?\}', '', game)  # remove all objects
    pgn = re.sub(r'\[.*?\]', '', pgn)
    pgn = re.sub(r"\d{1,2}\.\.\.", "", pgn)  # remove move numbers
    # pgn = re.sub(r"\s{2,3}", " ", pgn)  # remove move numbers
    pgn = re.sub(r"\+", "", pgn)  # remove check notation
    pgn.replace("\n", " ")
    pgn = pgn.strip()

    result = "Win" if (pgn[-3] == 1 and player_color == "White") or \
                      (pgn[-3] == 0 and player_color == "Black") else "Loss"  # Draws currently unsupported
    pgn = pgn[:-3:] # remove game resuts
    pgn = io.StringIO(pgn)
    chess_game = chess.pgn.read_game(pgn)
    moves = []
    for move in chess_game.mainline_moves():
        moves.append(move.uci())

    opening = game[game.index("\n[ECOUrl") + 10: game.index("\"]\n[UTCDate")]

    return {
        "match": moves,
        "player_color": player_color,
        "opening": opening,
        "result": result
    }