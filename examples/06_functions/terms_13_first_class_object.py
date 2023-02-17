"""
В Python все функции являются объектами первого класса.
Python поддерживает:
* передачу функций в качестве аргументов другим функциям
* возвращение функции как результата других функций
* присваивание функций переменным
* сохранение функций в структурах данных
"""
import time
from getpass import getpass
from rich import inspect


def check_passwd(username, password, *, min_length=8, check_username=True):
    if len(password) < min_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True

# check_passwd.test = True
# inspect(check_passwd, dunder=True)
# inspect(check_passwd.__code__, dunder=True)

def delay(seconds, func, *args, **kwargs):
    print(f"{args=} {kwargs=}")
    print(f"Delay {seconds} ...")
    time.sleep(seconds)
    return func(*args, **kwargs)


def select_prompt_func(param):
    func_choice = {
        "username": input,
        "password": getpass,
        "secret": getpass,
    }
    return func_choice.get(param, input)


class CiscoSSH:
    def __init__(self, **device_params):
        params = {
            "username": input,
            "password": getpass,
            "secret": getpass,
        }
        for param in params:
            if param not in device_params:
                function = params[param]
                device_params[param] = function(f"{param.capitalize()}: ")
