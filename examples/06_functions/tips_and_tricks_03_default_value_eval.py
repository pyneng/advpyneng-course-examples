from datetime import datetime
import time


def print_current_datetime():
    print(f">>> {datetime.now()}")


for i in range(3):
    print("Имитируем долгое выполнение...")
    time.sleep(1)
    print_current_datetime()

