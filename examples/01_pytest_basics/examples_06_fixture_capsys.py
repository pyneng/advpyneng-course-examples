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


@pytest.mark.parametrize("min_len, result", [(4, True), (8, False), (6, True)])
def test_check_passwd_min_length(min_len, result, capsys):
    user = "user1"
    password = "123456"
    assert check_passwd(user, password, min_length=min_len) == result
    out = capsys.readouterr().out
    if result == False:
        assert "короткий" in out
    else:
        assert "прошел все проверки" in out
