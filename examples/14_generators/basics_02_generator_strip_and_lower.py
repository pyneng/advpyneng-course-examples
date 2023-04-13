from pprint import pprint


def strip_and_lower1(items):
    result = []
    for item in items:
        result.append(str(item).strip().lower())
    return result


def strip_and_lower2(items):
    for item in items:
        yield str(item).strip().lower()


def strip_and_lower3(items):
    for item in items:
        item = str(item).strip().lower()
        yield item
        if "test" in item:
            yield 42
            return


data = ["\nUSER\r\n", "\tTEST\n", "Data"]
# for i in strip_and_lower(data):
#     pprint(i)
