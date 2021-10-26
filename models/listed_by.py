from tinydb import TinyDB
from tabulate import tabulate


class List:

    def list_order_players(self, order):
        self.order = int(order)
        p_tab = TinyDB('data/players.json').table('players')
        all_players = p_tab.all()
        list_players = []
        for i in range(len(all_players)):
            p_data = (
                all_players[i].get("surname"),
                all_players[i].get('name'),
                all_players[i].get('dob'),
                all_players[i].get('genre'),
                all_players[i].get('rank'),
                all_players[i].get('score')
            )
            list_players.append(p_data)
        if self.order == 1:
            list_a = sorted(list_players, key=lambda colonnes: colonnes[0])
        elif self.order == 2:
            list_a = sorted(list_players, key=lambda colonnes: int(colonnes[4]))
        first_colone = ("Nom", "Prénom", "Date de naissance", "Genre", "Classement","Score")
        list_a.insert(0, first_colone)
        print(tabulate(list_a))

    def list_order_tournaments(self):

        t_tab = TinyDB('data/tournaments.json').table('tournaments')
        all_tournaments = t_tab.all()
        list_tournaments = []
        for i in range(len(all_tournaments)):
            p_data_t = (
                all_tournaments[i].get('name'),
                all_tournaments[i].get('place'),
                all_tournaments[i].get('date'),
                all_tournaments[i].get('timing'),
                all_tournaments[i].get('description'),
                all_tournaments[i].get('nbr_round'),

            )
            list_tournaments.append(p_data_t)
        first_colone = ("Nom de tournoi", "Place", "Date", "Timing", "Description","Nombre de tours")
        list_tournaments.insert(0, first_colone)
        print(tabulate(list_tournaments))
