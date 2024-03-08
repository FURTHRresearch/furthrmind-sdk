from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.import_collection import *

class Project(BaseClass):
    id = ""
    name = ""
    info = ""
    shortid = ""
    samples = []
    experiments = []
    groups = []
    units = []
    researchitems = []
    permissions = []
    fields = []

    attr_definition = {
        "samples": {"class": "Sample"},
        "experiments": {"class": "Experiment"},
        "groups": {"class": "Group"},
        "units": {"class": "Unit"},
        "researchitems": {"class": "ResearchItem"},
        "fields": {"class": "Field"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)


    def _get_url(self, id=None):
        if id is None:
            return self.fm.get_project_url(self.id)
        else:
            return self.fm.get_project_url(id)

    @classmethod
    def _get_all_url(cls):
        return f"{cls.fm.base_url}/projects"

    @staticmethod
    def create():
        pass




