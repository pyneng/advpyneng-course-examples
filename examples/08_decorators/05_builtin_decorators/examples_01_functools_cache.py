from functools import cache, lru_cache


@cache
def factorial(n):
    print(f"{n=}")
    return n * factorial(n - 1) if n else 1


print(f"{factorial(4)=}")
print(f"{factorial(5)=}")
print(f"{factorial(6)=}")



def mycache(func):
    print("mycache")
    cache_dict = {}
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

