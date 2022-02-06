#!/usr/bin/env python
import re
import requests
import json


def get_user_game_archives_from_chess_dot_com(user: str):

    games = []
    headers = {
        'Content-type': 'application/json',
    }
    archives = json.loads(requests
                          .get(f'https://api.chess.com/pub/player/{user}/games/archives', headers=headers)
                          .content.decode('UTF-8'))["archives"]
    most_recent_month = json.loads(requests.get(archives[-1], headers=headers).content.decode('UTF-8'))
    most_recent_dirty_game = most_recent_month["games"][-3]

    cleaned_game = clean_game(most_recent_dirty_game["pgn"], user)
    return [cleaned_game]

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
    pgn = re.sub(r"\d{1,2}\.+", "", pgn)
    pgn.replace("\n", " ")  # This doesn't actually work!
    pgn = pgn.strip()

    result = "Win" if (pgn[-3] == 1 and player_color == "White") or \
                      (pgn[-3] == 0 and player_color == "Black") else "Loss"  # Draws currently unsupported
    pgn = pgn[:-5:]
    pgn = pgn.split("   ")

    white_moves = pgn[::2]
    black_moves = pgn[1::2]
    move_pairs = [list(pair) for pair in zip(white_moves, black_moves)]
    if len(white_moves) > len(black_moves):
        move_pairs.append([white_moves[-1]])
    opening = game[game.index("\n[ECOUrl") + 10: game.index("\"]\n[UTCDate")]

    return {
        "match": move_pairs,
        "player_color": player_color,
        "opening": opening,
        "result": result
    }