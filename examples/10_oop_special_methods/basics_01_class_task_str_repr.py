from datetime import datetime

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


t1 = Task("task1", due="15/09/2023")
t2 = Task("task2")
