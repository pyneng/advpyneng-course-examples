from typing import Optional, Iterable, Any, TypedDict


def check_passwd(
    username: str,
    password: str,
    min_length: int = 8,
    forbidden_symbols: Iterable[str] = "%",
) -> bool:
    if len(password) < min_length:
        return False
    elif set(forbidden_symbols) & set(password):
        return False
    else:
        return True


def prompt_password(
    username: str,
    password: Optional[str] = None,
    **kwargs: Any
) -> bool:
    if password is None:
        password = input("Введите пароль: ")
    return check_passwd(username, password, **kwargs)


if __name__ == "__main__":
    check_passwd("nata", "12345", min_length=3)
    check_passwd("nata", "12345nata", min_length=3)
    check_passwd("nata", "12345nata", min_length=3)
