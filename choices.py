import datetime
from services import (id_count,
                      new_data,
                      INCOME,
                      EXPENSE,
                      balance_update,
                      data_update,
                      category_search,
                      date_search,
                      summ_search, )


def user_choice_1() -> None:
    with open('balance.txt', 'r') as file:
        print(f'Текущий баланс: {file.read()}')


def user_choice_2() -> None:
    print('Варианты действий:')
    print('Новая запись с доходами: 1')
    print('Новая запись с расходами: 2')
    user_choice = input('Введите число 1 или 2: ')
    if user_choice == '1':
        new_description = input('Введите описание доходов: ')
        new_summ = input('Введите сумму: ')
        try:
            new_summ = int(new_summ)
        except ValueError:
            print('Ошибка ввода.')
            print('Введите целое число.')
            user_choice_2()
        new_operation_id = id_count()
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        new_data(
            description=new_description,
            summ=new_summ,
            operation_id=new_operation_id,
            op_name=INCOME,
            date=current_date
        )
        balance_update(
            summ=new_summ,
            op_name=INCOME,
        )

    elif user_choice == '2':
        new_description = input('Введите описание расходов: ')
        new_summ = input('Введите сумму: ')
        try:
            new_summ = int(new_summ)
        except ValueError:
            print('Ошибка ввода.')
            print('Введите целое число.')
            user_choice_2()
        new_operation_id = id_count()
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        new_data(
            description=new_description,
            summ=new_summ,
            operation_id=new_operation_id,
            op_name=EXPENSE,
            date=current_date
        )
        balance_update(
            summ=new_summ,
            op_name=EXPENSE,
        )

    else:
        print('Ошибка ввода!')
        print('Введите число 1 или 2')
        user_choice_2()


def user_choice_3() -> None:
    user_choice = input('Введите id записи для редактирования: ')
    data_update(
        choice=user_choice
    )


def user_choice_4() -> None:
    print('Введите 1 для поиска по категории')
    print('Введите 2 для поиска по дате')
    print('Введите 3 для поиска по сумме')
    user_choice = input('Введите параметр поиска: ')
    if user_choice == '1':
        print('Укажите категорию для поиска:')
        print('Введите 1 для поиска доходов')
        print('Введите 2 для поиска расходов')
        user_input = input('Введите категорию для поиска: ')
        if user_input == '1':
            category_search(
                category=INCOME,
            )
        elif user_input == '2':
            category_search(
                category=EXPENSE,
            )
        else:
            print('Ошибка ввода!')
            print('Введите целое число от 1 до 2')

    elif user_choice == '2':
        user_input = input('Введите дату для поиска: ')
        date_search(
            date=user_input,
        )
    elif user_choice == '3':
        user_input = input('Введите сумму для поиска: ')
        try:
            user_input = int(user_input)
        except ValueError:
            print('Ошибка ввода.')
            print('Введите целое число.')
            user_choice_4()

        summ_search(
            summ=int(user_input),
        )
    else:
        print('Ошибка ввода!')
        print('Введите целое число от 1 до 3')
        user_choice_4()


def all_choices(user_choice: str) -> None:
    if user_choice == '1':
        user_choice_1()

    elif user_choice == '2':
        user_choice_2()

    elif user_choice == '3':
        user_choice_3()

    elif user_choice == '4':
        user_choice_4()

    else:
        print('Ошибка ввода!')
        print('Введите целое число от 1 до 4')



