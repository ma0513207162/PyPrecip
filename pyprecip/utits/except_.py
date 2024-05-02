class RaiseException():
    def __init__(self, message, category):
        self._message = message
        self._category = category

    @staticmethod 
    def raise_exception(message: str = "error", category:type = Exception):
        instance = RaiseException(message, category)
        instance.raise_exception_impl() 

    def raise_exception_impl(self):
        raise self._category(self._message)


# if __name__ == "__main__": 
#     RaiseException.raise_exception("hello,world", Exception)






