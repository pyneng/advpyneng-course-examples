"""
В Python все функции являются объектами первого класса.
Python поддерживает:
* создание функций в runtime
* передачу функций в качестве аргументов другим функциям
* возвращение функции как результата других функций
* присваивание функций переменным, сохранение функций в структурах данных
"""
from rich import inspect


def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True


check_passwd.test = True
inspect(check_passwd, dunder=True)
inspect(check_passwd.__code__, dunder=True)
