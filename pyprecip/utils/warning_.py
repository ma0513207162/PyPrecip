import warnings
from .export_ import export 

@export
class CustomWarn():
    def __init__(self) -> None:
        pass 

    def raise_warning(message = "warnning", warning_type = Warning):
        warnings.warn(message, warning_type)