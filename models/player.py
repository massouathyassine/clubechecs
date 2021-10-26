from tinydb import TinyDB, Query
class Player:

    def __init__(self, id=None):
        self.id = id
        self.name = ''
        self.surname = ''
        self.dob = ''
        self.genre = ''
        self.score = ''
        self.rank = ''
        if id:
            self.get_player(id)

    def get_player(self, id):
        q = Query()
        data = TinyDB('data/players.json').table(
            'players').search(q.id == id)
        self.name = data[0]['name']
        self.surname = data[0]['surname']
        self.dob = data[0]['dob']
        self.genre = data[0]['genre']
        self.rank = data[0]['rank']
        self.score = data[0]['score']

    def update_score(self, score):

        q = Query()
        p_tab = TinyDB('data/players.json').table('players').search(q.id == self.id)
        total_score = p_tab[0]['score'] + score
        p_tab = TinyDB('data/players.json').table('players')
        p_tab.update({"score": total_score}, q.id == self.id)


