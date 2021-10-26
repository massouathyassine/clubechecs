import datetime
from views import menu


class Input:

    def select_menu(self, len_menu):
        self.len_menu = len_menu
        self.number_menu = 0
        while self.number_menu < 1:
            try:
                self.number_menu = int(input('Tapez un choix : '))
                if self.number_menu < 1:
                    print('Erreur')
                elif self.number_menu > int(self.len_menu):
                    print('Erreur')
                    self.number_menu = 0

            except ValueError:
                print('Erreur')
                self.number_menu = 0
        return self.number_menu

    def verification_input(self, input_type, input_text):

        self.input_type = input_type

        if self.input_type == 'text':
            self.input = str(input(input_text)).upper()
            while (len(self.input) == 0):
                self.input = str(input(input_text)).upper()
            return self.input

        elif self.input_type == 'genre':
            while True:
                self.input = input(input_text).upper()
                if self.input == 'M' or self.input == 'F':
                    break
            return self.input

        elif self.input_type == 'number':
            self.input = -1
            while self.input < 0:
                try:
                    self.input = int(input(input_text))
                    if self.input < 0:
                        menu.View().errorMessage("err_number")
                except ValueError:
                    menu.View().errorMessage("d")
            return self.input

        elif self.input_type == 'date':
            while True:
                try:
                    self.input = input(input_text)
                    date = datetime.datetime.strptime(self.input, '%d/%m/%Y')
                    date = date.date()
                    break
                except ValueError:
                    menu.View().errorMessage("err_number")
            return self.input
