"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
"""


import copy
import sys
from constants import PLAYERS, TEAMS


if __name__ == "__main__":


    player_list = copy.deepcopy(PLAYERS)
    team_list = copy.deepcopy(TEAMS)
    num_players_team = int(len(player_list) / len(team_list))


    def clean_data():
        """copy player data to new list, save height as integer, save experience as boolean"""

        for player in player_list:
            player["height"] = int(player["height"].replace(' inches', ''))
            player["experience"] = bool(player["experience"].replace('NO', ''))


    def balance_teams():
        """divide players into balanced teams"""

        clean_data()

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
        first_choice_prompt = """
Here are your choices:
1) Display Team Stats
2) Quit
        """

        print(first_choice_prompt)

        try:
            choice = int(input("\nEnter an option > "))
        except ValueError:
            error_handler()

        if choice == 1:
            second_choice()
        elif choice == 2:
            print("\n\nThank you for using this app. Goodbye!")

            end_app()
        else:
            error_handler()


    def second_choice():
        """second choice prompt and logic to show team stats for specific team"""

        choice = None
        team_list_index = 0

        print("\n\nPick a team:")

        for team in team_list:
            team_list_index += 1
            print(f"{team_list_index}) {team}")

        try:
            choice = int(input("\nEnter an option > "))
        except ValueError:
            error_handler()

        if choice in range(1, len(team_list) + 1):
            team_index = choice - 1
            selected_team = team_list[team_index]
            player_printout = ""

            for player in player_list:
                player_name = player["name"]
                if player["team"] == selected_team:
                    player_printout += f"{player_name}, "

            player_printout = player_printout[:-2]

            stats = f"""
\n\nTeam: {team_list[team_index]} Stats
--------------------
Total players: {num_players_team}
\nPlayers on Team:
{player_printout}
            """
            
            print(stats)

            input("\nPress ENTER to continue...")

            first_choice()
        else:
            error_handler()


    def start_app():
        """start the app"""

        if len(player_list) % len(team_list) != 0:
            data_error = """
This app requires the number of players to be evenly divisble into the number of teams.
Please check the constants.py file to adjust the number of players or teams as needed.
After updating and saving the file, run this app again.
Thank you!
            """
            
            print(data_error)

            sys.exit()
        else:
            balance_teams()

        start_prompt = """
\n\nBASKETBALL TEAM STATS TOOL
\n\n----MENU----
        """

        print(start_prompt)

        first_choice()


    def end_app():
        """end the app"""

        print("\n\n----END----\n\n")

        sys.exit()


    start_app()
