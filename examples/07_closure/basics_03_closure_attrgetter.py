

def attrgetter(attr):
    def get_attr_from_obj(obj):
        return getattr(obj, attr)
    return get_attr_from_obj
