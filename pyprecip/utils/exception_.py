from exporter import export


@export
class CustomException():
    def __init__(self):
        pass 

    def raise_exception(self,message: str = "error", exception_type: type = Exception):
        raise exception_type(message) 
    

if __name__ == "__main__":
    pass 


