

class Base:
    def __init__(self, name):
        print("Base __init__")
        self.name = name

    def __repr__(self):
        return f"<{type(self).__name__} {self.name}>"


class Parent1(Base):
    def __init__(self, name):
        print("Parent1 __init__")
        self.name = name
        super().__init__(name)


class Parent2(Base):
    def __init__(self, name):
        print("Parent2 __init__")
        self.name = name
        super().__init__(name)


#        Base
#        ^   ^
#       /     \
#      /       \
#     /         \
# Parent1     Parent2
#     ^         ^
#      \       /
#       \     /
#        \   /
#        Child
