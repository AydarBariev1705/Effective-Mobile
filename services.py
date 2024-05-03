import json

INCOME = 'Доход'
EXPENSE = 'Расход'


def id_count() -> int:
    with open('id.txt', 'r') as f:
        cur_id = int(f.read())
    with open('id.txt', 'w') as f:
        cur_id += 1
        f.write(str(cur_id))
    return cur_id


def new_data(description: str, summ: int, operation_id: int, op_name: str, date: str) -> None:
    with open('history.json', 'r', encoding='utf-8', ) as json_file:
        old_data = json.load(json_file)
        old_data[operation_id] = {
            'Дата': date,
            'Категория': op_name,
            'Сумма': summ,
            'Описание': description,
        }
    with open('history.json', 'w', encoding='utf-8', ) as json_file:
        json.dump(
            old_data,
            json_file,
            indent=4,
            ensure_ascii=False
        )
    print('Запись успешно сохранена!')


def data_update(choice: str) -> None:
    with open('history.json', 'r', encoding='utf-8', ) as json_file:
        data = json.load(json_file)
        if choice not in data.keys():
            print('Запись не найдена')
        else:
            description = input('Введите новое описание: ')
            summ = int(input('Введите новую сумму: '))
            with open('history.json', 'r', encoding='utf-8', ) as json_file:
                old_data = json.load(json_file)
                update_data = old_data.get(choice)
                update_data['Сумма'] = summ
                update_data['Описание'] = description
                old_data[choice] = update_data

                with open('history.json', 'w', encoding='utf-8', ) as json_file:
                    json.dump(
                        old_data,
                        json_file,
                        indent=4,
                        ensure_ascii=False
                    )
            print('Запись успешно обновлена!')


def balance_update(summ: int, op_name: str) -> None:
    if op_name == INCOME:
        with open('balance.txt', 'r') as file:
            new_balanse = int(file.read()) + summ
    elif op_name == EXPENSE:
        with open('balance.txt', 'r') as file:
            new_balanse = int(file.read()) - summ

    with open('balance.txt', 'w') as file:
        file.write(str(new_balanse))
    print('Баланс обновлен!')


def date_search(date: str):
    with open('history.json', 'r', encoding='utf-8', ) as json_file:
        data = json.load(json_file)
    result = 0
    for key, value in data.items():
        if value.get('Дата') == date:
            print(f'{key}: {value}')
            result += 1

    print(f'Всего найдено результатов поиска: {result}')


def category_search(category: str):
    with open('history.json', 'r', encoding='utf-8', ) as json_file:
        data = json.load(json_file)
    result = 0
    for key, value in data.items():
        if value.get('Категория') == category:
            print(f'{key}: {value}')
            result += 1

    print(f'Всего найдено результатов поиска: {result}')


def summ_search(summ: int):
    with open('history.json', 'r', encoding='utf-8', ) as json_file:
        data = json.load(json_file)
    result = 0
    for key, value in data.items():
        if value.get('Сумма') == summ:
            print(f'{key}: {value}')
            result += 1

    print(f'Всего найдено результатов поиска: {result}')
