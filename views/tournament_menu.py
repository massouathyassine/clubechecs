from models import search
from views import input_views
import datetime


class TournamentInput:

    def input_tournaments(self):

        self.id = str(datetime.datetime.now())
        self.played = 1
        self.rounds={}
        self.tournament_name = input_views.Input().verification_input(
            'text', 'Name of tournament: '
        )
        self.tournament_place = input_views.Input().verification_input(
            'text', 'Place of tournament: '
        )
        self.tournament_date = input_views.Input().verification_input(
            'date', 'Date of tournament: '
        )
        self.tournament_rounds = input_views.Input().verification_input(
            'number', 'Number of round (4 default): '
        )

        self.players_added = []
        print("\n1 >> Bullet \n2 >> Blitz \n3 >> Coup rapide\n")
        self.menu_number = input_views.Input().select_menu(3)
        if self.menu_number == 1:
            self.tournament_timing = 'BULLET'
        elif self.menu_number == 2:
            self.tournament_timing = 'BLITZ'
        elif self.menu_number == 3:
            self.tournament_timing = 'COUP RAPIDE'

        self.tournament_description = input_views.Input().verification_input(
            'text', 'Description: '
        )
        while True:
            print('\nFind player to be added :  ')
            self.find_player = search.Search().search_player(
                input_views.Input().verification_input('text', 'Name or first name: ')
            )
            if self.find_player == 'None':
                pass
            else:
                self.players_added.append(self.find_player)
                print('Player added')
            if len(self.players_added) == 8:
                break

        return {
            "id": self.id,
            "name": self.tournament_name,
            "place": self.tournament_place,
            "date": self.tournament_date,
            "timing": self.tournament_timing,
            "description": self.tournament_description,
            "players": self.players_added,
            "nbr_round": self.tournament_rounds,
            "played": self.played,
            "rounds": self.rounds
        }

