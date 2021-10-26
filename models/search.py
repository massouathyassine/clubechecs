from tinydb import Query, TinyDB

class Search:

    def search_player(self, name):
        """ Find player in DB, return player id or None """
        self.name = name
        q = Query()
        data = TinyDB('data/players.json').table('players')

        self.search_result = data.search(
            (q.name == self.name) |
            (q.surname == self.name)
        )

        if len(self.search_result) == 0:
            print("Player not found")
            return 'None'

        elif len(self.search_result) >= 1:
            for i in range(len(self.search_result)):
                print(
                    i+1, '>>', self.search_result[i]['name'], self.search_result[i]['surname'],
                    self.search_result[i]['dob'], '- Classement actuel:', self.search_result[i]['rank']
                )
            self.num_player = int(input('Tapez un choix : '))
            return self.search_result[self.num_player-1]['id']

    def search_tournament(self, name):
        """ Find tournament in DB, return tournament id or None """
        self.name = name
        q = Query()
        data = TinyDB('data/tournaments.json').table('tournaments')

        self.search_result = data.search(
            (q.name == self.name) |
            (q.place == self.name)
        )

        if len(self.search_result) == 0:
            print("Tournament not found")
            return 'None'
        elif len(self.search_result) >= 1:
            for i in range(len(self.search_result)):
                print(
                    i + 1, '>>', "Le tournoi : ", self.search_result[i]['name'], " à ", self.search_result[i]['place']
                )
            self.player_number = int(input('Tapez un choix : '))
            return self.search_result[self.player_number - 1]['id']