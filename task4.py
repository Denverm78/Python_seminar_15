# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

import logging
from datetime import datetime

logging.basicConfig(filename="result_4.log", filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def text_to_date(text):
    # text = input("Введите текст: ")
    logger.info(text)
    year = datetime.today().year
    month = text.split(" ")[2]
    weekDay = text.split(" ")[1]
    dayNumber = int(text.split(" ")[0].split("-")[0])
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


if __name__ == '__main__':
    text_to_date("3-й четверг ноября")
    text_to_date("1-й четверг ноября")
    text_to_date("2-я среда августа")