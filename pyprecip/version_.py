"""Tools for versioning."""

def get_version():
    from importlib.metadata import distribution, PackageNotFoundError
    
    try: 
        dist = distribution(__package__)

        print(dist)
    except PackageNotFoundError:
        return "Unknown"


get_version() 