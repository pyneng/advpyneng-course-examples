from rich import inspect

def check_passwd(user, passwd, min_len=8, unique_numbers=3):
    """
	Проверяет пароль и возвращает True если пароль правильный и False иначе.
    Args:
        user: имя пользователя
        passwd: пароль
        min_len: минимальное количество символов в пароле
        unique_numbers: количество уникальных цифр в пароле
    Returns:
        True: пароль прошел все проверки
        False: пароль не прошел одну из проверок
    """
    user = str(user)
    passwd = str(passwd)
    numbers = set("0123456789")
    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(passwd) & numbers) < unique_numbers:
        return False
    else:
        return True


print(check_passwd("user1", "pass3245word"))
print(check_passwd("admin", "adminpass3565word", min_len=10))

