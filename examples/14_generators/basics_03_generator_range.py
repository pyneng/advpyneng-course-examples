# 10_oop_special_methods/basics_09_class_range_iterator.py

def my_range(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1
