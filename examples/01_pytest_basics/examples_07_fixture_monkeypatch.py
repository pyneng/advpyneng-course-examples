import pytest


def check_passwd(username, password, min_length=8):
    if len(password) < min_length:
        print("Пароль слишком короткий")
        return False
    elif username.lower() in password.lower():
        print("Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} прошел все проверки")
        return True


def prompt_passwd(username, password=None, **kwargs):
    if password is None:
        password = input("Введите пароль: ")
    return check_passwd(username, password, **kwargs)


def test_prompt_passwd(monkeypatch):
    def myinput(prompt=None):
        return "12346128742"

    monkeypatch.setattr("builtins.input", myinput)
    # monkeypatch.setattr("builtins.input", lambda prompt=None: "203987928734")
    assert prompt_passwd("user1") == True


@pytest.mark.parametrize(
    "user, passwd, min_len, correct_result",
    [
        ("user1", "123user1w456", 8, False),
        ("user1", "123453245346", 6, True),
    ],
)
def test_check_passwd_param(
    user, passwd, min_len, correct_result, monkeypatch
):
    monkeypatch.setattr("builtins.input", lambda prompt=None: passwd)
    assert prompt_passwd(user, min_length=min_len) == correct_result


@pytest.mark.parametrize(
    "user, passwd, min_len, correct_result",
    [
        ("user1", "123user1w456", 8, False),
        ("user1", "123453245346", 6, True),
    ],
)
def test_check_passwd_param_2(
    user, passwd, min_len, correct_result, monkeypatch
):
    def myinput(prompt=None):
        return passwd

    monkeypatch.setattr("builtins.input", myinput)

    assert prompt_passwd(user, min_length=min_len) == correct_result
