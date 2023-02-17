"""
В Python все функции являются объектами первого класса.
Python поддерживает:
* создание функций в runtime
* передачу функций в качестве аргументов другим функциям
* возвращение функции как результата других функций
* присваивание функций переменным, сохранение функций в структурах данных
"""
from getpass import getpass
from rich import inspect


def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True


def select_request_function(param):
    choice = {
        "username": input,
        "password": getpass,
        "secret": getpass,
    }
    return choice.get(param, input)

check_passwd.test = True
inspect(check_passwd, dunder=True)
inspect(check_passwd.__code__, dunder=True)


class CiscoSSH:
    def __init__(self, **device_params):
        params = {
            "username": input,
            "password": getpass,
            "secret": getpass,
        }
        for param in params:
            if not param in device_params:
                function = params[param]
                device_params[param] = function(f"{param.capitalize()}: ")

