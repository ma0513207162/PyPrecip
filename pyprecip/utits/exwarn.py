import warnings



def raise_exception(message: str = "error", exception_type: type = Exception):
    raise exception_type(message)  

def raise_warning(message = "warnning", warning_type = Warning):
    print("=" * 20)
    warnings.warn(message, warning_type)
 
    






