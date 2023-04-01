from abc import ABC, ABCMeta, abstractmethod


# class BaseFilter(metaclass=ABCMeta):
#     pass


class BaseFilter(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def filter(self):
        print("BaseFilter filter")

    def filter_all(self):
        for item in self.data:
            print(item)
            self.filter()
