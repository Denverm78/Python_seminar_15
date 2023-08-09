# Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки. 📌 При этом значение любого параметра можно опустить. 
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, # но и числовые, т.е не мая, а 5.

import argparse
import logging
from datetime import datetime

logging.basicConfig(filename="result_5.log", filemode='w', encoding='utf-8', level=logging.INFO) 
logger = logging.getLogger(__name__)

def split_str(text):
    split_text = text.split(' ')
    print(split_text)
    month = split_text[2]
    weekDay = split_text[1]
    day = split_text[0]
    text_to_date(month, weekDay, day)

def text_to_date(month: str, weekDay: str, day: str):
    # text = input("Введите текст: ")
    logger.info([day, weekDay, month])
    year = datetime.today().year
    dayNumber = int(day.split("-")[0])
    if month.isdigit():
        monthNumber = int(month)
    else:
        monthDict = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6, "июля": 7, "августа": 8,
                    "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
        monthNumber = monthDict[month]
    weekDict = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3, "пятница": 4, "суббота": 5, "воскресенье": 6}
    weekDayNumber = weekDict[weekDay]
    dayMonth = 1
    count = 0
    for i in range(1, 32):
        myDate = datetime.date(datetime(year, monthNumber, i))
        dayName = datetime.weekday(myDate)
        if dayName == weekDayNumber:
            count += 1
            if count == dayNumber:
                dayMonth = i
                break
    result = f'{dayMonth}.{monthNumber}.{year}' 
    print(result)
    logger.info(result)

def parser_func():
    parser = argparse.ArgumentParser(description='Преобразовываем текст в дату в текущем году')
    parser.add_argument('dayNumber', default='1')
    parser.add_argument('weekDay', default=datetime.now().weekday())
    parser.add_argument('month', default=datetime.now().month)
    args = parser.parse_args()
    text_to_date(args.month, args.weekDay, args.dayNumber)


if __name__ == '__main__':
    
    parser_func()
       
    # python .\task5.py 1-й четверг ноября
    # python .\task5.py 1-й четверг 11
    # split_str('1-й четверг ноября')
    # split_str('1-й четверг 11')
    # split_str('3-я пятница июля')