from datetime import datetime
import time


def print_current_datetime(ptime=None):
    if ptime is None:
        ptime = datetime.now()
    print(f">>> Time {ptime}")


# for _ in range(3):
#     print_current_datetime()
#     time.sleep(3)


def to_str(src_items, result_list=None):
    if result_list is None:
        result_list = []
    for item in src_items:
        result_list.append(str(item))
    return result_list


def to_str(src_items):
    print(f"{id(src_items)=}")
    for i in range(len(src_items)):
        src_items[i] = str(src_items[i])
    return src_items


data = [100, 200, 300]
print(f"before {data=} {id(data)=}")
print(to_str(data))
print(f"after {data=}")
