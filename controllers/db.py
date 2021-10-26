from tinydb import TinyDB, where



def save_db(db_name, serialized_data):
    db = TinyDB("data/" + db_name + ".json").table(db_name)
    db.insert(serialized_data)
    print(f"{serialized_data['name']} sauvegardé avec succès.")


def edit_ranking(id, new_rank):
    query = Query()
    date = TinyDB('data/players.json').table('players')
    date.update({"rank": new_rank}, query.id == id)

