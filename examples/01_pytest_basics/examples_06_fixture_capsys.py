import pytest
from pprint import pprint


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


@pytest.mark.parametrize(
    "user, passwd, min_len, correct_result",
    [
        ("user1", "123456", 6, True),
        ("user1", "123456", 8, False),
    ],
)
def test_check_passwd_min_len(user, passwd, min_len, correct_result, capsys):
    assert check_passwd(user, passwd, min_len) == correct_result
    out = capsys.readouterr().out
    if correct_result:
        assert user in out
    else:
        assert "Пароль слишком короткий" in out


@pytest.mark.parametrize(
    "user, passwd, min_len, correct_result",
    [
        ("user1", "123user1w456", 8, False),
        ("user1", "123453245346", 6, True),
    ],
)
def test_check_passwd_user_in_passwd(
    user, passwd, min_len, correct_result, capsys
):
    assert check_passwd(user, passwd, min_len) == correct_result
    out = capsys.readouterr().out
    if correct_result:
        assert user in out
    else:
        assert "Пароль содержит имя пользователя" in out
