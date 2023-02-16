
def sum_arg(*args):
    print(args)
    sum_num = 0
    for arg in args:
        sum_num += arg
    return sum_num

"""
In [1]: sum_arg(1, 2)
(1, 2)
Out[1]: 3

In [2]: sum_arg(1)
(1,)
Out[2]: 1

In [3]: sum_arg(1, 10, 20, 30)
(1, 10, 20, 30)
Out[3]: 61

In [4]: sum_arg()
()
Out[4]: 0
"""
