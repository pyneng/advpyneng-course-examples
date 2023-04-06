from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass(order=True)
class Task:
    title: str
    description: Optional[str] = field(default=None, repr=False)
    due: Optional[datetime] = None

    def __post_init__(self):
        if self.due is None:
            self.due = datetime.now().date()
        else:
            self.due = datetime.strptime(self.due, "%d/%m/%Y").date()
