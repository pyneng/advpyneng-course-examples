

class Filter:
    def __init__(self, function, iterable):
        self.function = function
        self._items = iter(iterable)

    def __next__(self):
        print("__next__")
        while True:
            value = next(self._items)
            if self.function(value):
                return value

    def __iter__(self):
        print("__iter__")
        return self

