from functools import total_ordering
from datetime import datetime
from tabulate import tabulate


@total_ordering
class Task:
    def __init__(self, title, description=None, due=None):
        self.title = title
        self.description = description
        if due is None:
            self.due = datetime.now().date()
        else:
            self.due = datetime.strptime(due, "%d/%m/%Y").date()

    def __lt__(self, other):  # <
        print(f"Task __lt__ {self=} {other=}")
        if not isinstance(other, Task):
            return NotImplemented
        return self.due < other.due

    def __eq__(self, other):  # ==
        print(f"Task __eq__ {self=} {other=}")
        if not isinstance(other, Task):
            return NotImplemented
        return (self.title, self.description, self.due) == (
            other.title, other.description, other.due,
        )

    def __str__(self):
        return f"{self.__class__.__name__}({'self.title'})"

    def __repr__(self):
        return f"<{self.__class__.__name__} title='{self.title}' due={self.due}>"
