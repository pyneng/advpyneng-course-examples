from functools import wraps


def cache_decorator(maxsize=10):
    def mycache(func):
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

    if isinstance(maxsize, int):
        return mycache
    elif callable(maxsize):
        function = maxsize
        return mycache(function)
    else:
        raise TypeError("...")
