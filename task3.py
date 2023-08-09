# Доработаем задачу 2. 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


import logging
from datetime import datetime

logging.basicConfig(filename="result.log", filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def superLogger(func):
    def wrapper(*args, **kwargs):
        dict = {}
        dict["level"] = logger.level
        dict["function"] = func.__name__
        dict["arguments"] = [*args]
        result = func(*args, **kwargs)
        dict["result"] = result
        # dt = datetime.now() 
        # dict["data_time"] = dt
        logger.info(dict)
        logger.info(datetime.now())
        return result
    return wrapper

@superLogger
def sum_ever(x, y):
    return x + y


if __name__ == '__main__':
    print(sum_ever (5, 10))