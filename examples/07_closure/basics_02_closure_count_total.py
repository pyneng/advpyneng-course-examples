def count_total(start_value):
    print(f"count_total {start_value=}")
    total = [start_value]

    def inner(add_number):
        print(f"inner {add_number=}")
        total.append(add_number)
        return sum(total)

    return inner


def count_total(start_value):
    print(f"count_total {start_value=}")
    total = start_value

    def inner(add_number):
        print(f"inner {add_number=}")
        nonlocal total
        total += add_number
        # total = total + add_number
        return total

    return inner
