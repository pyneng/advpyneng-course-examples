url_func_dict = {}


def route(link):
    print(f"route {link}")
    def decorator(func):
        print(f"decorator {func}")
        url_func_dict[link] = func
        return func

    return decorator


@route("/")
def index():
    pass


# decorator = route("/")
# index = decorator(index)


@route("/pyneng")
def pyneng_func():
    pass


print(url_func_dict)
