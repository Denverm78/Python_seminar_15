# Решить задачи, которые не успели решить на семинаре.
# 📌 Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров.

# Откорректировал 4-ю задачу - добавил логирование и счетчик для правильной работы (task4.py)
# Сделал пятую задачу (task5.py)
# Сделал домашнюю задачу vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

import argparse
import logging

logging.basicConfig(filename="result_7.log", filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def _check_year(year): 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True 
    else: 
        return False

def check_date(date_str):
    logger.info(date_str)
    LONG_MONTH = [1, 3, 5, 7, 8, 10, 12]
    SHORT_MONTH = [4, 6, 9, 11]
    FEBRUARY = 2
    DAY_LONG_MONTH = 31
    DAY_SHORT_MONTH = 30
    DAY_LONG_FEBRUARY = 29
    DAY_SHORT_FEBRUARY = 28
    date_list = []
    for n in date_str.split("."):
        date_list.append(int(n))

    if 1 <= date_list[2] <= 9999:
        if date_list[1] in LONG_MONTH:
            if 1 <= date_list[0] <= DAY_LONG_MONTH:
                return True
            else: return False
        elif date_list[1] in SHORT_MONTH:
            if 1 <= date_list[0] <= DAY_SHORT_MONTH:
                return True
            else: return False    
        elif date_list[1] == FEBRUARY:
            if _check_year(date_list[2]) == True:
                if 1 <= date_list[0] <= DAY_LONG_FEBRUARY:
                    return True
                else: return False
            else: 
                if 1 <= date_list[0] <= DAY_SHORT_FEBRUARY:
                    return True
                else: return False
        else: return False
    else: return False

def parser_func():
    parser = argparse.ArgumentParser(description='Проверяем существует ли указанная дата')
    parser.add_argument('user_data', metavar='Data', type=str, nargs='*', help='Введите дату в формате DD.MM.YEAR')
    args = parser.parse_args()
    original_str = args.user_data[0]
    print_result(original_str)
    
def print_result(orig_str):
    result = check_date(orig_str)
    logger.info(result)
    if result == True:
        print(f'Дата {orig_str} существует')
    else:
        print(f'Дата {orig_str} не существует')


if __name__ == '__main__':

    # user_date = input("Введите дату в формате DD.MM.YYYY: ")
    # print(check_date(user_date))
    # python .\hw_task7.py 22.03.2023
    # python .\hw_task7.py 22.13.2023 
    parser_func()