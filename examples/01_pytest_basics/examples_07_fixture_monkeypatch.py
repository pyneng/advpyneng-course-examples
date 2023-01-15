import getpass


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


def prompt_password(username, password=None, **kwargs):
    if password is None:
        # password = input("Введите пароль: ")
        password = getpass.getpass()

    return check_passwd(username, password, **kwargs)


def test_prompt_password_input(monkeypatch):
    # monkeypatch.setattr('builtins.input', lambda prompt=None: '123456789')
    monkeypatch.setattr(getpass, "getpass", lambda x=None: '123456789')
    assert prompt_password("user1", None) == True
