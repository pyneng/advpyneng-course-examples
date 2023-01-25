from pprint import pprint
import time
from typing import Protocol, runtime_checkable

@runtime_checkable
class Readable(Protocol):
    def read(self, amount: int) -> str: ...


class FileStream:
    def __init__(self, filename: str):
        self.filename = filename
        self.stream = open(self.filename)

    def read(self, amount: int) -> str:
        return self.stream.read(amount)


def read_stream(stream: Readable, part_size: int) -> None:
    while True:
        part = stream.read(part_size)
        if part:
            pprint(part)
            time.sleep(0.2)
        else:
            break


if __name__ == "__main__":
    f = FileStream("output/sh_cdp_n_det.txt")
    read_stream(f, 100)
