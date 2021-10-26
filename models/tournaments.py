from tinydb import TinyDB, Query
from models.player import Player
import datetime
from views.menu import View
from views.input_views import Input
from tabulate import tabulate


class Tournament:

    def __init__(self, id=None):
        self.name = ''
        self.place = ''
        self.date = ''
        self.timing = ''
        self.players = []
        self.nbr_round = ''
        self.rounds = []
        self.description = ''
        self.played = ''
        self.id = id
        if id:
            self.get_tournament(id)

    def get_tournament(self, id):

        q = Query()
        data = TinyDB('data/tournaments.json').table(
            'tournaments').search(q.id == id)
        self.name = data[0]['name']
        self.place = data[0]['place']
        self.date = data[0]['date']
        self.nbr_round = data[0]['nbr_round']
        self.timing = data[0]['timing']
        self.description = data[0]['description']
        self.players = data[0]['players']
        self.played = data[0]['played']
        self.rounds = data[0]['rounds']

    def generate_match(self, round):
        # liste des players de 1er tour
        if round == 1:
            list_players = []
            for i in range(len(self.players)):
                self.player = Player(self.players[i])
                p_data = (
                    self.player.id,
                    self.player.rank
                )
                list_players.append(p_data)
            list_sorted_by_rank = sorted(
                list_players, key=lambda colonnes: int(colonnes[1]), reverse=True
            )
            final_players_list = []
            for i in range(4):
                final_players_list.append(list_sorted_by_rank[i][0])
                final_players_list.append(list_sorted_by_rank[i + 4][0])

            return (final_players_list)

        # liste des players de tour suivant
        else:
            # Tri par score
            list_players = []
            for i in range(len(self.players)):
                self.player = Player(self.players[i])
                p_data = (
                    self.player.id,
                    self.player.score
                )
                list_players.append(p_data)

            list_players_score = sorted(
                list_players, key=lambda colonnes: colonnes[1], reverse=True
            )
            # Tri par classement si score egal
            list_players_ranked = []
            while len(list_players_score) > 1:
                if list_players_score[0][1] == list_players_score[1][1]:
                    list_players_for_rank = []
                    while True:
                        try:
                            if (
                                    list_players_score[0][1] ==
                                    list_players_score[1][1]
                            ):
                                list_players_for_rank.append(
                                    list_players_score[0][0]
                                )
                                list_players_score.pop(0)
                            else:
                                list_players_for_rank.append(
                                    list_players_score[0][0]
                                )
                                list_players_score.pop(0)
                                break
                        except IndexError:
                            list_players_for_rank.append(
                                list_players_score[0][0]
                            )
                            list_players_score.pop(0)
                            break

                    temp_list_players = []
                    for i in range(len(list_players_for_rank)):
                        self.player = Player(
                            list_players_for_rank[i]
                        )
                        p_data = ()
                        p_data = (
                            self.player.id,
                            self.player.rank
                        )
                        temp_list_players.append(p_data)

                    temp_list_players_ranked = sorted(
                        temp_list_players, key=lambda colonnes: int(colonnes[1]),
                        reverse=True
                    )
                    for i in range(len(temp_list_players_ranked)):
                        list_players_ranked.append(
                            temp_list_players_ranked[0][0]
                        )
                        temp_list_players_ranked.pop(0)
                else:
                    list_players_ranked.append(list_players_score[0][0])
                    list_players_score.pop(0)
            try:
                list_players_ranked.append(list_players_score[0][0])
                list_players_score.pop(0)
            except IndexError:
                pass

            return list_players_ranked

    def start_round(self):

        self.players_list = self.generate_match(self.played)
        self.round_start = datetime.datetime.now().strftime("%H:%M:%S")
        self.match = 1
        self.player_id = 0
        self.players_score = []
        while self.match < 5:

            self.player1 = Player(self.players_list[self.player_id])
            self.player_id += 1
            self.player2 = Player(self.players_list[self.player_id])
            self.player_id += 1
            View().current_round(self.played, self.match, self.player1, self.player2)

            self.choice_win = Input().select_menu(3)

            if self.choice_win == 1:

                self.player1.update_score(1)
                self.player1_score = 1
                self.player2_score = 0

            elif self.choice_win == 2:

                self.player2.update_score(1)
                self.player1_score = 0
                self.player2_score = 1
            elif self.choice_win == 3:

                self.player1.update_score(0.5)
                self.player2.update_score(0.5)
                self.player1_score = 0.5
                self.player2_score = 0.5

            self.match += 1
            self.players_score.append([
                [self.player1.id, self.player1_score],
                [self.player2.id, self.player2_score]
            ])
        self.round_end = datetime.datetime.now().strftime("%H:%M:%S")
        self.rounds[self.played] = {
            'time': [self.round_start, self.round_end],
            'matchs': self.players_score
        }
        self.played += 1
        q = Query()
        tab_t = TinyDB('data/tournaments.json').table('tournaments')
        tab_t.update({"played": self.played}, q.id == self.id)
        tab_t.update({"rounds": self.rounds}, q.id == self.id)

    def list_players(self, order):

        self.order = order
        list_players = []
        for i in range(len(self.players)):
            player = Player(self.players[i])
            p_data = ()
            p_data = (
                player.surname,
                player.name,
                player.genre,
                player.rank,
                player.score
            )
            list_players.append(p_data)

        if self.order == 1:
            list_a = sorted(list_players, key=lambda colonnes: colonnes[0])
        elif self.order == 2:
            list_a = sorted(
                list_players, key=lambda colonnes: int(colonnes[3]), reverse=False
            )
        elif self.order == 3:
            list_a = sorted(
                list_players, key=lambda colonnes: colonnes[4], reverse=True
            )

        first_colone = ("Nom", "Prénom", "Genre", "Classement", "Score")
        list_a.insert(0, first_colone)
        print(tabulate(list_a))


    def list_tours(self):

        for list_tours in range((len(self.rounds))):
            list_tours_ = str(list_tours+1)
            print("\n")
            print(" << Round  " + str(list_tours+1)+" >>" +"\n")

            for list_matchs in range(len(
                    self.rounds[list_tours_]['matchs']
            )):
                player1 = Player(
                    self.rounds[list_tours_]['matchs'][list_matchs][0][0]
                )
                player2 = Player(
                    self.rounds[list_tours_]['matchs'][list_matchs][1][0]
                )
                print("["+player1.name+"]" , self.rounds[list_tours_]['matchs'][list_matchs][0][1] ," : ",self.rounds[list_tours_]['matchs'][list_matchs][1][1], "["+player2.name+"]")


