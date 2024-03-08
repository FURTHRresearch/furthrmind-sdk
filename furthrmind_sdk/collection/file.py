from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.baseclass import BaseClass

class File(BaseClass):
    id = ""
    name = ""

    attr_definition = {
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    @classmethod
    def get(cls, id=None):
        raise TypeError("Not implemented")

    @classmethod
    def get_all(cls):
        raise TypeError("Not implemented")


    #todo implement as class and instance method
    @classmethod
    def download(cls, id=None):
        pass

    @classmethod
    def upload(cls):
        pass

    #todo implement as class and instance method
    @classmethod
    def update_file(cls, id=None):
        pass




