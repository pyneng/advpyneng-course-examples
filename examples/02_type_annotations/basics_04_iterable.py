

def convert_to_lower(items: list[str]) -> list[str]:
    result = []
    for item in items:
        result.append(item.lower())
    return result


if __name__ == "__main__":
    print(convert_to_lower(["A", "B", "C"]))
    print(convert_to_lower({"A", "B", "C"}))
    print(convert_to_lower(("A", "B", "C")))
