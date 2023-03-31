class Base:
    pass


class Parent1(Base):
    pass


class Parent2(Base):
    pass


class Child(Parent1, Parent2):
    pass


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
