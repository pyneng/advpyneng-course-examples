from functools import wraps


def mycache(function=None, *, maxsize=10):
    def decorator(func):
        print("mycache")
        cache_dict = {}

        @wraps(func)
        def inner(*args):
            if args in cache_dict:
                print("Читаем cache")
                return cache_dict[args]
            else:
                print("Что-то новое")
                result = func(*args)
                cache_dict[args] = result
                return result

        return inner

    if function is None:
        return decorator
    elif callable(function):
        return decorator(function)
    else:
        raise TypeError("...")


# @mycache
# sum = mycache(sum)

# @mycache(maxsize=10)
# decorator = mycache(maxsize=10)
# sum = decorator(sum)

