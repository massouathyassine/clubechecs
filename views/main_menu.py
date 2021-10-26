from views import menu
from views import player_menu
from views.input_views import Input
from views.menu import View
from models import search
from models import listed_by
from models.tournaments import Tournament
from controllers.db import save_db
from controllers.player import edit_ranking
from views import tournament_menu
from models import tournaments
from controllers.tournament import get_tournament


class MainMenu:

    def main_menu(self):
        menu.View().main_menu()
        self.menu_number = Input().select_menu("3")

        # Call player menu
        if self.menu_number == 1:
            MainMenu().players_menu()

        # Call tournaments menu
        elif self.menu_number == 2:
            MainMenu().tournaments_menu()

        # Close app
        elif self.menu_number == 3:
            pass

    def players_menu(self):

        menu.View().players_menu()

        self.menu_number = Input().select_menu("5")

        #  Call for create player
        if self.menu_number == 1:

            serialized_new_player = player_menu.PlayerInput().input_players()
            print(serialized_new_player)
            save_db("players" , serialized_new_player)
            MainMenu().players_menu()

        elif self.menu_number == 2:

            name_or_surname = input("Nom ou Prénom : ")
            self.find_player = search.Search().search_player(name_or_surname.upper())

            if self.find_player == 'None':
                print("Player not found")

            else:

                print(self.find_player)
                new_rank = input('Nouveau classement: ')
                edit_ranking(self.find_player, new_rank)
                print("New rank saved")
                MainMenu().players_menu()

        elif self.menu_number == 3:
            print("\n\
1 >> List ordrer by alphabetic.\n\
2 >> List  ordrer de rank.\n")
            self.choix_order = input('Choix de liste : ')
            listed_by.List().list_order_players(self.choix_order)
            MainMenu().players_menu()
        elif self.menu_number == 4:
            MainMenu().main_menu()
        elif self.menu_number == 5:
            pass

    def tournaments_menu(self):
        menu.View().tournaments_menu()
        self.menu_number = Input().select_menu("5")
        if self.menu_number == 1:

            serialized_new_tournament = tournament_menu.TournamentInput().input_tournaments()
            print(serialized_new_tournament)
            save_db("tournaments", serialized_new_tournament)
            menu.View().tournaments_menu()

        elif self.menu_number == 2:
            name_or_place = input("Nom ou Place : ")
            self.find_tournament = search.Search().search_tournament(name_or_place.upper())
            if self.find_tournament == 'None':
                pass
            else:
                MainMenu().tournament_menu_play(self.find_tournament)
        elif self.menu_number == 3:
            listed_by.List().list_order_tournaments()
            self.tournaments_menu()
        elif self.menu_number == 4:
            MainMenu().main_menu()
        elif self.menu_number == 5:
            pass

    def tournament_menu_play(self, id_tournament):
        self.tournament1 = Tournament(id_tournament)
        View.menu_tournament_play(self, self.tournament1.name, self.tournament1.date, self.tournament1.nbr_round, self.tournament1.played)
        self.menu_number = int(input("Tapez un choix: "))

        if self.menu_number == 1:
            self.tournament1.start_round()
            self.tournament1.played += 1
            self.tournament_menu_play(self.tournament1.id)
        elif self.menu_number == 2:
            View.menu_order_by(self)
            choix_order = Input().select_menu(3)
            self.tournament1.list_players(choix_order)
            self.tournament_menu_play(self.tournament1.id)
        elif self.menu_number==3:
            self.tournament1.list_tours()
        elif self.menu_number == 4:
            MainMenu().tournaments_menu()
        elif self.menu_number == 5:
            pass




