class View:

    def main_menu(self):
        print('\n')
        print('[ Home ]')
        print("\n\
1 >> Menu Player\n\
2 >> Menu Tournaments.\n\
3 >> Exit.\n")

    def players_menu(self):
        print('\n')
        print('[ Players ]')
        print("\n\
1 >> Add Player.\n\
2 >> Edit Player.\n\
3 >> List of Players.\n\
4 >> Return.\n\
5 >> Exit.\n")

    def tournaments_menu(self):
        print('\n')
        print('[ Tournaments ]')
        print("\n\
1 >> Add Tournament.\n\
2 >> Play a Tournament.\n\
3 >> List of Tournaments.\n\
4 >> Return.\n\
5 >> Exit.\n")

    def save_player(self, name, surname):
        print(
            '\nLe joueur', name,
            surname, 'a était sauvegardé avec succès !'
        )

    def modify_player(self, surname, name, birth, rank):
        print(
            '\nMise à joueur de:', surname, name,
            birth, '(Nouveau classement:', rank, ')'
        )

    def menu_tournament_play(self, name, date, rounds, played):
        print('\n')
        print('[', name, ']')
        print("Date de tournoi", ': ', date)
        if played > rounds:
            print('\nLe tournoi est terminé.')
        else:
            print("\n1 >> Démarrer le tours n°", played)
        print("\
2 >> List of Players\n\
3 >> List Rounds & Matchs\n\
4 >> Return\n\
5 >> Close\n")

    def current_round(self, round, match, player1, player2):
        print('\n \nTour', round, '- Match', match)
        print(
            player1.name, player1.surname,
            'contre', player2.name, player2.surname
        )
        print('\nRésultats:')
        print('\n1 >>', player1.name, player1.surname, 'gagnant')
        print('2 >>', player2.name, player2.surname, 'gagnant')
        print('3 >> Match nul\n')

    def menu_order_by(self):
        print("\n\
1 >> Order by alphabetic\n\
2 >> Order by rank\n\
3 >> Order by score\n")
