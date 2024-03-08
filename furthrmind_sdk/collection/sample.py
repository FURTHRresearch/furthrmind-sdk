from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.baseclass import BaseClassWithFieldData

class Sample(BaseClassWithFieldData):
    id = ""
    name = ""
    neglect = False
    shortid = ""
    files = []
    fielddata = []
    linked_experiments = []
    linked_samples = []
    linked_researchitems = {}
    groups = []
    datatables = []

    attr_definition = {
        "files": {"class": "File"},
        "fielddata": {"class": "FieldData"},
        "groups": {"class": "Group"},
        "linked_samples": {"class": "Sample"},
        "linked_experiments": {"class": "Experiment"},
        "linked_researchitems": {"class": "ResearchItem", "nested_dict": True},
        "datatables": {"class": "DataTable"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def _get_url(self, id=None, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        if id is None:
            url = f"{project_url}/samples/{self.id}"
        else:
            url = f"{project_url}/samples/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/samples"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/samples"
        return url

    @staticmethod
    def create():
        pass




