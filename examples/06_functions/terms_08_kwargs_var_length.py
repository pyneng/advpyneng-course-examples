

def sum_arg(a, b, **kwargs):
    print(f"{kwargs=}")
    sum_num = 0
    for arg in kwargs.values():
        sum_num += arg
    return sum_num
