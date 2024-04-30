__all__ = {} 


def export(obj): 
    __all__[obj.__name__] = obj 
    return obj 


