

def attr_getter(attr):
    def inner(obj):
        return getattr(obj, attr)
    return inner
