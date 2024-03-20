from furthrmind_sdk.collection.baseclass import BaseClassWithFieldData, BaseClassWithFiles, BaseClassWithGroup, BaseClass
from typing_extensions import Self, Dict, List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from furthrmind_sdk.collection import *


class Sample(BaseClassWithFieldData, BaseClassWithFiles, BaseClassWithGroup):
    id = ""
    name = ""
    neglect = False
    shortid = ""
    files: List["File"] = []
    fielddata: List["FieldData"] = []
    linked_experiments: List["Experiment"] = []
    linked_samples: List[Self] = []
    linked_researchitems: Dict[str, List["ResearchItem"]] = {}
    groups: List["Group"] = []
    datatables: List["DataTable"] = []

    _attr_definition = {
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

    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name, group_name=None, group_id=None, project_id=None) -> Self:
        """
        Method to create a new sample
        :param name: the name of the item to be created
        :param group_name: The name of the group where the new item will belong to. group name can be only considered
                            for groups that are not subgroups. Either group_name or group_id must be specified
        :param group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return instance of the sample class
        """
        return Sample._create(name, group_name, group_id, project_id)

    @classmethod
    @BaseClass._create_instances_decorator
    def create_many(cls, data_list: List[Dict], project_id=None) -> Self:
        """
        Method to create multiple samples
        :param data_list: dict with the following keys:
            - name: the name of the item to be created
            - group_name: The name of the group where the new item will belong to. group name can be only considered
                            for groups that are not subgroups. Either group_name or group_id must be specified
            - group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return list with instance of the sample class
        """
        return Sample._create_many(data_list, project_id)



