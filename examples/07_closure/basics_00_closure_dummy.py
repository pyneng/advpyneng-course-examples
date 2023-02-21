
def out_func():
    free_var_1 = 42

    def in_func():
        return free_var_1 * 10

    return in_func
