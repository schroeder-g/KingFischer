#!/usr/bin/env python
import os


from get_all_user_games import get_user_game_archives_from_chess_dot_com
archive = get_user_game_archives_from_chess_dot_com(user="checkmatejunky")
for game in archive:
    # find_mistakes(game)
    print(game)
    # print(game['match'])
    print(os.environ['USERPROFILE'])

