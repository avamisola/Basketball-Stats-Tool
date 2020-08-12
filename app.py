"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
"""


from constants import TEAMS, PLAYERS


if __name__ == "__main__":


    def clean_data():
        """copy player data to new list, save height as integer, save experience as boolean"""

        player_list = []

        for player in PLAYERS:
            player_list.append(player)

        for player in player_list:
            player["height"] = int(player["height"].replace(' inches', ''))
            player["experience"] = bool(player["experience"].replace('NO', ''))

        print(player_list)

    clean_data()
