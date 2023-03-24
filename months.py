import random as r

months = {
    'polish':
        {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec',
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


while True:
    option = int(input('Which option do you want to choose?'
                       '\n1. Show months. '
                       '\n2. Try to print correct month. '
                       '\n3. Exit\n'))

    if option == 1:
        language = input('Which language? ').lower()
        if language in months.keys():
            print(months[language])
        else:
            print('You have only 5 lists of polish, english, russian, ukrainian, italian months.')

    elif option == 2:
        keys_or_values = int(input('Do you want to print num by knowing name(1) or name by knowing num(2): '))
        if keys_or_values == 1:
            language = input('Which language? ').lower()
            score = 0
            for _ in range(5):
                if language in months:
                    random_month = months[language][r.randint(1, 12)]
                    answer = int(input(f'{random_month}: '))
                    if 0 < answer < 13:
                        if random_month == months[language][answer]:
                            print(True)
                            score += 1
                        else:
                            print(False)
                    else:
                        print('Your answer must be int type 1-12 num. ')
            print(f'Your score is {score}/5')
        elif keys_or_values == 2:
            language = input('Which language? ').lower()
            score = 0
            for _ in range(5):
                if language in months:
                    random_month = r.randint(1, 12)
                    answer = input(f'{random_month}: ').title()
                    if answer in months[language].values():
                        if answer == months[language][random_month]:
                            print(True)
                            score += 1
                        else:
                            print(False)
                    else:
                        print('This month is not exist. ')
            print(f'Your score is {score}/5')
