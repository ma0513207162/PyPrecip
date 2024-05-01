import warnings
from package_tools import Exporter


exporter = Exporter(globals())
 
@exporter.export
def raise_exception(message: str = "error", exception_type: type = Exception):
    raise exception_type(message)  

@exporter.export
def raise_warning(message = "warnning", warning_type = Warning):
        warnings.warn(message, warning_type)
 
    






