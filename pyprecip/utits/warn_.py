import warnings

 
class RaiseWarn():
    def __init__(self, message, category):
        self._message = message; 
        self._category = category
        warnings.formatwarning = self.custom_formatwarning

    def custom_formatwarning(self, message_, category_, filename, lineno, line):
        custom_format = f"PyPrecip {category_.__name__}: {message_} ({filename}:{lineno})\n"
        return custom_format            
                
    @staticmethod
    def raise_warning(message: str = "warnning", category: type = Warning):
        instance = RaiseWarn(message, category)
        instance.raise_warning_impl()
        
    def raise_warning_impl(self):
        warnings.warn(self._message, category=self._category) 



if __name__ == "__main__": 
    # test 
    RaiseWarn.raise_warning("warning message", UserWarning)









