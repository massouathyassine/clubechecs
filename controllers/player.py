from controllers.db import save_db
from models.player import Player
from views.player_menu import PlayerInput
from tinydb import TinyDB, Query


def create_player():
    # Récupération des infos du joueur
    user_entries = PlayerInput().input_players()

    # Création du joueur
    player = Player(
        user_entries['id'],
        user_entries['name'],
        user_entries['first_name'],
        user_entries['date_of_birthay'],
        user_entries['genre'],
        user_entries['score'],
        user_entries['rank'])

    # serialization:
    serialized_player = player.serialized_player()
    print(serialized_player)

    # Sauvegarde du joueur dans la database
    save_db("players", serialized_player)

    return player


def edit_ranking(id, new_rank):
    query = Query()
    date = TinyDB('data/players.json').table('players')
    date.update({"rank": new_rank}, query.id == id)
