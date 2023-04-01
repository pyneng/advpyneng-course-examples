from tabulate import tabulate
from class_task import Task


class TodoList:
    def __init__(self, tasks=None):
        if tasks is None:
            self._tasks = []
        else:
            self._tasks = list(tasks)

    def __repr__(self):
        return f"<{self.__class__.__name__} tasks={len(self._tasks)}>"

    def __str__(self):
        if not self._tasks:
            return f"{repr(self)}. You're all done!"
        table = [vars(task) for task in self._tasks]
        return tabulate(table, headers="keys")

    def __getitem__(self, index):
        print(f"__getitem__ {index=}")
        return self._tasks[index]

    def __setitem__(self, index, value):
        print(f"__setitem__ {index=} {value=}")
        self._tasks[index] = value

    def __delitem__(self, index):
        print(f"__delitem__ {index=}")
        del self._tasks[index]

    def __len__(self):
        return len(self._tasks)

    def append(self, item):
        self._tasks.append(item)


t1 = Task("task1", due="25/03/2023")
t2 = Task("task2", due="28/03/2023")
t3 = Task("task3", due="22/03/2023")
t4 = Task("task4", due="27/03/2023")
t5 = Task("task5", due="29/03/2023")
