import time
import asyncio
from datetime import datetime


async def print_num(name):
    print(f"Start {name}")
    for _ in range(10):
        print(42)
        time.sleep(0.5)
    print(f"End {name}")


async def print_text(name):
    print(f"Start {name}")
    for _ in range(10):
        print("test")
        await asyncio.sleep(0.8)
    print(f"End {name}")


async def main():
    await asyncio.gather(print_num("task1"), print_text("task2"))
