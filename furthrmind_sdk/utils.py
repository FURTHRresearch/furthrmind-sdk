from functools import wraps
from types import MethodType

def furthr_wrap(f):
    @wraps(f)
    def decorated(*args, **kws):
        response = f(*args, **kws)
        if response.status_code != 200:
            return "error", response.status_code
        data = response.json()
        if data["status"] == "error":
            print("error", data["message"])
            raise ValueError(data["message"])
        else:
            if len(data["results"]) == 1:
                return data["results"][0]
            else:
                return data["results"]
    return decorated

def instance_overload(self, methods):
    """ Adds instance overloads for one or more classmethods"""
    for name in methods:
        setattr(self, name, MethodType(getattr(self, name).__func__, self))
