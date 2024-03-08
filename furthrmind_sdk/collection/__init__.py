from furthrmind_sdk.collection.import_collection import *

def get_collection_class(collection_name):
    return eval(collection_name)
