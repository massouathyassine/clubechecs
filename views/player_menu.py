from views import input_views
import datetime


class PlayerInput:

    def input_players(self):
        """ Input for create player & return inputs """
        self.id = str(datetime.datetime.now())
        self.name = input_views.Input().verification_input('text', 'Name: ')
        self.surname = input_views.Input().verification_input('text', 'First name: ')
        self.dob = input_views.Input().verification_input(
            'date', 'Date de birthay: ')
        self.genre = input_views.Input().verification_input('genre', 'F ou M: ')
        self.rank = input_views.Input().verification_input('number', 'Rank: ')

        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "dob": self.dob,
            "genre": self.genre,
            "score": 0,
            "rank": self.rank,
        }
