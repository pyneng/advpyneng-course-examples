import time
from datetime import datetime


class RunningTime:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        self.start = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"__exit__ {exc_type=} {exc_value=} {traceback=}")
        self.stop = datetime.now()
        print(f"Running time: {self.stop - self.start}")


with RunningTime():
    time.sleep(2)

with RunningTime() as run:
    print("-" * 10)
    time.sleep(2)


run = RunningTime()
with run:
    print("-" * 10)
    time.sleep(2)


