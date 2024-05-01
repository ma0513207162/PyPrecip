import warnings
from package_tools import Exporter


exporter = Exporter(globals())
 
@exporter.export
def raise_exception(self, message: str = "error", exception_type: type = Exception):
    raise exception_type(message)  

"""
class CustomWarn():
    def __init__(self) -> None:
        pass 

    def raise_warning(message = "warnning", warning_type = Warning):
        warnings.warn(message, warning_type)

class CustomException():
    def __init__(self):
        pass 
    
    def raise_exception(self, message: str = "error", exception_type: type = Exception):
        raise exception_type(message)
"""
 
    






