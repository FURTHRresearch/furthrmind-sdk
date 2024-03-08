from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.baseclass import BaseClassWithFieldData

class ComboBoxEntry(BaseClassWithFieldData):
    id = ""
    name = ""
    files = []
    fielddata = []

    attr_definition = {
        "files": {"class": "File"},
        "fielddata": {"class": "FieldData"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)


    def _get_url(self, id=None, project_id=None):
        project_url = self.fm.get_project_url(project_id)
        if id is None:
            url = f"{project_url}/comboboxentry/{self.id}"
        else:
            url = f"{project_url}/comboboxentry/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/comboboxentry"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/comboboxentry"
        return url

    @staticmethod
    def create():
        pass




