from tinydb import TinyDB, Query


def play_tournament(tournament):
    print("Début de tournoi : " + tournament.name)
    nb_rounds_to_play = tournament.rounds_nbr
    for i in range(nb_rounds_to_play):
        tournament.create_round()


def get_tournament(id_tournament):
    q = Query()
    data = TinyDB('data/tournaments.json').table(
        'tournaments').search(q.id == id_tournament)
    name = data[0]['name']
    date = data[0]['date']
    rounds = data[0]['nbr_round']
    played = data[0]['played']

    return name, date, rounds, played
