while True:
    mes = input('Введите номер месяца от 1 до 12: ')
    if mes.isdigit() and 0 <= int(mes) <= 12:
    # if 0 <= int(user_month) <= 12 and user_month.isdigit():
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список сезонов - {season_1[int(mes) // 3]}\nСловарь сезонов - {season_2[int(mes) // 3]}')
        break
    else:
        print('Ошибка')
