class Test:
    def __init__(self, name):
        self.name = name
        self.timeout = 2

    def method1(self):
        print("method1")


class ChildTest(Test):
    def method2(self):
        print("method2")

    def __call__(self):
        print("Call...")


def summ(a, b):
    print(f"{a=} {b=}")
    return a + b
