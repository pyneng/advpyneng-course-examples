# 10_oop_special_methods/basics_10_class_filter_iterator.py
items = [100, None, 20, None, "test"]
filter(lambda x: x != None, items)


def my_filter(function, iterable):
    for item in iterable:
        if function(item):
            yield item
