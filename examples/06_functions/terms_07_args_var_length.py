
def sum_arg(a, b, *args, c, d):
    print(f"{a=} {b=} {args=} {c=} {d}")
    sum_num = 0
    for arg in args:
        sum_num += arg
    return sum_num

