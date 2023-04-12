import random as r

months = {
    'polish':
        {1: 'Styczen', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec',
         7: 'Lipiec', 8: 'Sierpień', 9: 'Wrzeszeń', 10: 'Pażdziernik', 11: 'Listopad', 12: 'Grudzień'},
    'english':
        {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
         8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'},
    'russian':
        {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
         8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'},
    'ukrainian':
        {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень', 7: 'Липень',
         8: 'Серпень', 9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'},
    'italian':
        {1: 'Gennaio', 2: 'Febbraio', 3: 'Marzo', 4: 'Aprile', 5: 'Maggio', 6: 'Giugno', 7: 'Luglio',
         8: 'Agosto', 9: 'Settembre', 10: 'Ottobre', 11: 'Novembre', 12: 'Dicembre'}
}


class Game:
    def __init__(self, choice):
        self.choice = choice
        self.score = 0

    def choose(self):
        while True:
            self.score = 0
            for _ in range(5):
                if self.choice == 1:
                    self.choice_1()
                else:
                    self.choice_2()
            else:
                print(f'Your score is {self.score}/5')
                try_again = input('Do you want to try again? (y/n) ')
                if try_again.lower() == 'n':
                    break

    def choice_1(self):
        random_month = months[language][r.randint(1, 12)]
        answer = int(input(f'{random_month}: '))
        if 0 < answer < 13:
            if random_month == months[language][answer]:
                print(True)
                self.score += 1
            else:
                print(False)
        else:
            print('Your answer must be int type 1-12 num. ')

    def choice_2(self):
        random_month = r.randint(1, 12)
        answer = input(f'{random_month}: ').lower().title()
        if answer in months[language].values():
            if answer == months[language][random_month]:
                print(True)
                self.score += 1
            else:
                print(False)
        else:
            print("There's is no such month")


while True:
    try:
        option = int(input('Which option do you want to choose?'
                           '\n1. Show months. '
                           '\n2. Try to print correct month. '
                           '\n3. Exit\n'))

        if option == 1:
            language = input('Which language? ').lower()
            if language in months.keys():
                print(months[language])
            else:
                print('You have only 5 available languages: polish, english, russian, ukrainian, italian.')

        elif option == 2:
            keys_or_values = int(input('Do you want to print num by knowing name(1) or name by knowing num(2): '))
            language = input('Which language? ').lower()
            if language in months:
                game = Game(keys_or_values)
                game.choose()
            else:
                print('You have only 5 available languages: polish, english, russian, ukrainian, italian.')

        elif option == 3:
            break

    except KeyboardInterrupt:
        print('Program was stopped')
        break
    except ValueError:
        print('Not correct command')
