# На семинаре про декораторы был создан логирующий декоратор. 
# Он сохранял аргументы функции и результат её работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging

logging.basicConfig(filename="result.log", filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def superLogger(func):
    def wrapper(*args, **kwargs):
        dict = {}
        dict["arguments"] = [*args]
        result = func(*args, **kwargs)
        dict["result"] = result
        logger.info(dict)
        return result
    return wrapper

@superLogger
def sum_ever(x, y):
    return x + y


if __name__ == '__main__':
    print(sum_ever (5, 10))    