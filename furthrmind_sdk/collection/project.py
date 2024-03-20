from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.baseclass import BaseClass
from typing import TYPE_CHECKING
from typing_extensions import List, Dict, Self
if TYPE_CHECKING:
    from furthrmind_sdk.collection import *

class Project(BaseClass):
    id = ""
    name = ""
    info = ""
    shortid = ""
    samples: List["Sample"] = []
    experiments: List["Experiment"] = []
    groups: List["Group"] = []
    units: List["Unit"] = []
    researchitems: Dict[str, List["ResearchItem"]] = {}
    permissions = []
    fields: List["Field"] = []

    _attr_definition = {
        "samples": {"class": "Sample"},
        "experiments": {"class": "Experiment"},
        "groups": {"class": "Group"},
        "units": {"class": "Unit"},
        "researchitems": {"class": "ResearchItem", "nested_dict": True},
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

    @classmethod
    def _post_url(cls):
        return f"{cls.fm.base_url}/projects"

    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name: str) -> Self:
        """
        Method to create a new project
        :param name: Name of the new project
        :return: instance of the project class
        """

        if not name:
            raise ValueError("Name is required")
        data = {"name": name}
        id = cls.post(data)
        data["id"] = id
        return data




