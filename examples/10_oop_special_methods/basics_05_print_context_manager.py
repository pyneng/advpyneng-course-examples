

class SuppressException:
    stats = {"suppressed": 0, "missed": 0}


    def __init__(self, *exceptions):
        print("__init__")
        self.exceptions = exceptions

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"__exit__ {exc_type=} {exc_value=} {traceback=}")
        if exc_type in self.exceptions:
            print(f"Suppressing exception {exc_type}...")
            self.stats["suppressed"] += 1
            return True
        else:
            self.stats["missed"] += 1

