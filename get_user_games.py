#!/usr/bin/env python
import re
import requests
import json


def get_user_game_archives(user: str):
    def clean_game(game: str):
        cleaned = {}
        cleaned["color"] = game[game.index(user) - 7: game.index(user) - 2]
        cleaned["opening"] = game[game.index("\n[ECOUrl") + 10: game.index("\"]\n[UTCDate")]
        obj_pattern = r'\{.*?\}'
        bracket_pattern = r'\[.*?\]'
        pgn = re.sub(r'\{.*?\}', '', game)
        pgn = re.sub(r'\[.*?\]', '', pgn)
        pgn = re.sub(r"\d\.+", "", pgn)
        pgn.replace("\n", " ")
        cleaned["result"] = "Win" if pgn[-4] == 1 and cleaned["color"] == "White" or \
                                     pgn[-4] == 0 and cleaned["color"] == "Black" else "Loss"
        print("Vals", pgn[-4:-1])
        cleaned["pgn"] = pgn
        cleaned["pgn"].replace("\n", "")
        return cleaned

    games = []
    headers = {
        'Content-type': 'application/json',
    }
    archives = json.loads(requests
                          .get(f'https://api.chess.com/pub/player/{user}/games/archives', headers=headers)
                          .content.decode('UTF-8'))["archives"]
    most_recent_month = json.loads(requests.get(archives[-1], headers=headers).content.decode('UTF-8'))
    most_recent_dirty_game = most_recent_month["games"][-1]
    cleaned_game = clean_game(most_recent_dirty_game["pgn"])
    print(cleaned_game)

    # for url in range(len(archives)):
    #     month_of_games = json.loads(requests
    #                                 .get(archives[url], headers=headers)
    #                                 .content.decode('UTF-8'))
    #     for game in range(len(month_of_games)):
    #
