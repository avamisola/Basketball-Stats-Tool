"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
"""


import copy
from constants import PLAYERS, TEAMS


if __name__ == "__main__":


    player_list = copy.deepcopy(PLAYERS)
    team_list = copy.deepcopy(TEAMS)


    def clean_data():
        """copy player data to new list, save height as integer, save experience as boolean"""

        for player in player_list:
            player["height"] = int(player["height"].replace(' inches', ''))
            player["experience"] = bool(player["experience"].replace('NO', ''))


    def balance_teams():
        """divide number of players by number of teams"""

        clean_data()

        num_players_team = int(len(player_list) / len(team_list))
        start_slice = 0
        end_slice = num_players_team
        player_list_index = 0
        team_list_index = 0
        balancing = True
        
        while balancing:

            for player in player_list[start_slice:end_slice]:
                player_list_index += 1
                player["team"] = team_list[team_list_index]
                #print(player)

                if player_list_index == end_slice:
                    if int(team_list_index) == int(len(team_list)) - 1:
                        balancing = False
                    else:
                        start_slice += num_players_team
                        end_slice += num_players_team
                        team_list_index += 1


        #print(num_players_team)
        #print(len(player_list))
        #print(len(TEAMS))
        #print(PLAYERS)

    balance_teams()
