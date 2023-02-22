func_dict = {}


def register(func):
    print(f"register {func=}")
    func_dict[func.__name__] = func
    return func


@register
def upper(string):
    print(f"upper {string=}")
    return string.upper()

# upper = register(upper)


@register
def lower(string):
    print(f"lower {string=}")
    return string.lower()


def capitalize(string):
    print(f"capitalize {string=}")
    return string.capitalize()


print(func_dict)
print(upper("test"))
