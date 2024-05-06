from choices import all_choices


def main_func():
    """
    Главная функция приложения.
    Используется для запуска приложения
    """

    print('Вас приветствует приложение "Личный финансовый кошелек" ')
    while True:
        print('\nВарианты действий:')
        print('Узнать баланс: 1')
        print('Добавление записи: 2')
        print('Редактирование записи: 3')
        print('Поиск по записям: 4\n')
        choice = input('Введите число 1, 2, 3 или 4: ')
        all_choices(
            user_choice=choice)


if __name__ == '__main__':
    main_func()
