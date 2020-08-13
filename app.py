"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
"""


import copy
import sys
from constants import PLAYERS, TEAMS


player_list = copy.deepcopy(PLAYERS)
team_list = copy.deepcopy(TEAMS)


if __name__ == "__main__":


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

                if player_list_index == end_slice:

                    if int(team_list_index) == int(len(team_list)) - 1:
                        balancing = False
                    else:
                        start_slice += num_players_team
                        end_slice += num_players_team
                        team_list_index += 1


    def error_handler():
        """generic error message and reroute to first choice"""

        print("\n\nThat is not a valid option, please choose again.")
        first_choice()


    def first_choice():
        """first choice prompt and logic to show team stats or quit app"""

        choice = None
        first_choice_prompt = """\nHere are your choices:
        1) Display Team Stats
        2) Quit
        """

        print(first_choice_prompt)

        try:
            choice = int(input("\nEnter an option > "))
        except ValueError:
            error_handler()

        if choice == 1:
            print("\n\nTime to sleep!")
            #second_choice = input("\nEnter an option > ")
            end_app()
        elif choice == 2:
            print("\n\nThank you for using this app. Goodbye!")
            end_app()
        else:
            error_handler()


    def start_app():
        """start the app"""

        balance_teams()

        start_prompt = """
        \n\nBASKETBALL TEAM STATS TOOL
        \n----MENU----
        """

        print(start_prompt)

        first_choice()


    def end_app():
        """end the app"""
        print("\n\n----END----\n\n")
        sys.exit()


    start_app()