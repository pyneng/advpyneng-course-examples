def dummy(number: int | None = None) -> int:
    # reveal_type(number)
    if number is None:
        number = 0
    return number * 100


if __name__ == "__main__":
    print(dummy(100))
    print(dummy())
