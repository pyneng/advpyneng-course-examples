import time


class RunningTime:
    def __enter__(self):
        print("__enter__")
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__", exc_type, exc_value, traceback)
        self.stop = time.time()
        print(f"Running time: {self.stop - self.start}")


t = RunningTime()

with t:
    time.sleep(2)

with RunningTime() as rtime:
    time.sleep(2)

print(rtime.start)
print(rtime.stop)

