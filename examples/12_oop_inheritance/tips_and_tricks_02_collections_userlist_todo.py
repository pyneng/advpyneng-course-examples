from tabulate import tabulate
from class_task import Task
from collections import UserList


class TodoList(UserList):
    def __repr__(self):
        return f"<{self.__class__.__name__} tasks={len(self.data)}>"

    def __str__(self):
        if not self.data:
            return f"{repr(self)}. You're all done!"
        table = [vars(task) for task in self.data]
        return tabulate(table, headers="keys")


t1 = Task("task1", due="25/03/2023")
t2 = Task("task2", due="28/03/2023")
t3 = Task("task3", due="22/03/2023")
t4 = Task("task4", due="27/03/2023")
t5 = Task("task5", due="29/03/2023")
