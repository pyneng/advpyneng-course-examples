def multiply(num1):
    print(f"multiply {num1=}")

    def inner(num2):
        print(f"inner {num1=} {num2=}")
        return num1 * num2

    return inner
