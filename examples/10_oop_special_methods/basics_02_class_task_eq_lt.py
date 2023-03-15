from functools import total_ordering
from datetime import datetime

@total_ordering
class Task:
    def __init__(self, title, description=None, due=None):
        self.title = title
        self.description = description
        if due is None:
            self.due = datetime.now().date()
        else:
            self.due = datetime.strptime(due, "%d/%m/%Y").date()

    def __str__(self):
        return f"{self.__class__.__name__}({'self.title'})"

    def __repr__(self):
        return f"<{self.__class__.__name__} title='{self.title}' due={self.due}>"

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
            other.title,
            other.description,
            other.due,
        )


class Dummy:
    def __eq__(self, other):
        print(f"Calling Dummy __eq__ {self=} {other=}")
        return NotImplemented

    def __ne__(self, other):
        print(f"Calling Dummy __ne__ {self=} {other=}")
        return NotImplemented

    def __lt__(self, other):
        print(f"Calling Dummy __lt__ {self=} {other=}")
        return NotImplemented

    def __gt__(self, other):
        print(f"Calling Dummy __gt__ {self=} {other=}")
        return NotImplemented

    def __le__(self, other):
        print(f"Calling Dummy __le__ {self=} {other=}")
        return NotImplemented

    def __ge__(self, other):
        print(f"Calling Dummy __ge__ {self=} {other=}")
        return NotImplemented


t1 = Task("task1", due="25/03/2023")
t2 = Task("task2")
