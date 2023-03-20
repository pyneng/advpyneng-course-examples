
class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self._current = start

    def __next__(self):
        print("__next__")
        value = self._current
        if value == self.stop:
            raise StopIteration
        self._current += 1
        return value

    def __iter__(self):
        print("__iter__")
        return self
