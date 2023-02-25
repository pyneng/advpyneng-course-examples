from functools import wraps


# def all_str_old(func):
#    @wraps(func)
#    def inner(*args):
#        if not all(isinstance(arg, str) for arg in args):
#            raise ValueError("Все аргументы должны быть строками")
#        return func(*args)
#
#    return inner
#
#
# @all_str_old
# def upper(string):
#    return string.upper()


def arg_type(required_type):
    print(f"create decorator for type {required_type}")

    def decorator(func):
        print(f"decorate {func}")

        @wraps(func)
        def inner(*args):
            print("inner")
            if not all(isinstance(arg, required_type) for arg in args):
                raise ValueError(f"Все аргументы должны быть {required_type.__name__}")
            return func(*args)

        return inner

    return decorator


all_str = arg_type(str)
all_int = arg_type(int)


@all_str
def upper(string):
    return string.upper()


# decorator = arg_type(str)
# upper = decorator(upper)


@all_str
def lower(string):
    print(f"lower {string=}")
    return string.lower()


@all_str
def capitalize(string):
    print(f"capitalize {string=}")
    return string.capitalize()
