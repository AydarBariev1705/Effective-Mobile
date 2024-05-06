import json

# Постоянные 'Доход' и 'Расход'
INCOME = 'Доход'
EXPENSE = 'Расход'


def id_count() -> int:
    """
    Функция для увеличения ID записи
    :return: int, Возвращает текущий id записи
    """
    try:
        with open('id.txt', 'r') as f:
            cur_id = int(f.read())
        with open('id.txt', 'w') as f:
            cur_id += 1
            f.write(str(cur_id))
    except (FileNotFoundError, ValueError):
        with open('id.txt', 'w+') as f:
            cur_id = 1
            f.write(str(cur_id))
    return cur_id


def new_data(description: str, summ: int, operation_id: int, op_name: str, date: str) -> None:
    """
    Функция для создания новой записи о расходах
    :param description: str, Описание новой записи
    :param summ: int, Сумма доходов или расходов у новой записи
    :param operation_id: int, id записи
    :param op_name: str, Категория записи
    :param date:  str, Дата записи
    :return: None
    """
    old_data = json_load()
    old_data[operation_id] = {
        'Дата': date,
        'Категория': op_name,
        'Сумма': summ,
        'Описание': description,
    }
    json_dump(old_data)
    print('Запись успешно сохранена!')


def data_update(choice: str) -> None:
    """
    Функция редактирования записи
    :param choice: str, Выбор клиента
    :return: None
    """
    data = json_load()
    if choice not in data.keys():
        print('Запись не найдена')
    else:
        description = input('Введите новое описание: ')
        summ = int(input('Введите новую сумму: '))
        old_data = json_load()
        update_data = old_data.get(choice)
        update_data['Сумма'] = summ
        update_data['Описание'] = description
        old_data[choice] = update_data

        json_dump(old_data)
        print('Запись успешно обновлена!')


def date_search(date: str) -> None:
    """
    Функция поиска по дате
    :param date: str, Дата записи
    :return: None
    """
    data = json_load()
    result = 0
    for key, value in data.items():
        if value.get('Дата') == date:
            print(f'{key}: {value}')
            result += 1

    print(f'Всего найдено результатов поиска: {result}')


def category_search(category: str) -> None:
    """
    Функция поиска по категории
    :param category: str, Категория записи
    :return: None
    """
    data = json_load()
    result = 0
    for key, value in data.items():
        if value.get('Категория') == category:
            print(f'{key}: {value}')
            result += 1

    print(f'Всего найдено результатов поиска: {result}')


def summ_search(summ: int) -> None:
    """
    Функция поиска по категории
    :param summ: int, Сумма записи
    :return: None
    """
    data = json_load()
    result = 0
    for key, value in data.items():
        if value.get('Сумма') == summ:
            print(f'{key}: {value}')
            result += 1

    print(f'Всего найдено результатов поиска: {result}')


def current_balance() -> tuple:
    """
    Функция для отображения текущего баланса, доходов и расходов
    :return: tuple, Кортеж со значениями баланса, доходов и расходов
    """
    data = json_load()
    total_income = 0
    total_expense = 0

    for key, value in data.items():
        if value.get('Категория') == INCOME:
            total_income += value.get('Сумма')
        elif value.get('Категория') == EXPENSE:
            total_expense += value.get('Сумма')
    cur_balance = total_income - total_expense

    return cur_balance, total_income, total_expense


def json_load() -> dict:
    """
    Функция для выгрузки данных из json файла
    :return: dict, Словарь с записями о доходах и расходах
    """
    try:
        with open('history.json', 'r', encoding='utf-8', ) as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                data = {}
    except FileNotFoundError:
        with open('history.json', 'w+', encoding='utf-8', ) as json_file:
            data = {}
            json.dump(
                data,
                json_file,
                indent=4,
                ensure_ascii=False
            )

    return data


def json_dump(dump_dict: dict) -> None:
    """
    Функция для записи данных в json файл
    :param dump_dict: dict, Словарь с записями о доходах и расходах
    :return: None
    """

    with open('history.json', 'w', encoding='utf-8', ) as json_file:
        json.dump(
            dump_dict,
            json_file,
            indent=4,
            ensure_ascii=False
        )
