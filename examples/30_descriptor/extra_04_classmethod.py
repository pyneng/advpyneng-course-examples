class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        if hasattr(type(self.f), '__get__'):
            # This code path was added in Python 3.9
            # and was deprecated in Python 3.11.
            return self.f.__get__(cls, cls)
        return MethodType(self.f, cls)
