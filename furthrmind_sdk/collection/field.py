from furthrmind_sdk.collection.baseclass import BaseClass
from typing_extensions import List, Self, Dict, TYPE_CHECKING
from inspect import isclass
if TYPE_CHECKING:
    from furthrmind_sdk.collection.comboboxentry import ComboBoxEntry

class Field(BaseClass):
    id = ""
    name = ""
    type = ""
    script = ""
    comboboxentries: List["ComboBoxEntry"] = []

    _attr_definition = {
        "comboboxentries": {"class": "ComboBoxEntry"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def _get_url_instance(self, project_id=None):
        project_url = Field.fm.get_project_url(project_id)
        url = f"{project_url}/fields/{self.id}"
        return url

    @classmethod
    def _get_url_class(cls, id, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fields/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fields"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fields"
        return url

    @classmethod
    def get(cls, id=None, name=None) -> Self:
        """
        Method to get all one field by it's id
        :param str id: id of requested field 
        :param str name: name of requested field 
        :return Self: Instance of field class
        """
        

        if isclass(cls):
            if id is None:
                id = name
            assert id is not None or name is not None, "Either id or name must be specified"
            return cls._get_class_method(id)
        else:
            self = cls
            data = self._get_instance_method()
            return data
    
    @classmethod
    def get_all(cls, project_id=None) -> List[Self]:
        """
        Method to get all fields belonging to one project
        If called on an instance of the class, the id of the class is used
        :param str project_id: Optionally to get fields from another project as the furthrmind sdk was initiated with, defaults to None
        :return List[Self]: List with instances of field class
        """
        return super().get_all(project_id)
    
    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name, type, project_id=None) -> Self:
        """
        Method to create a new sample

        :param name: the name of the field to be created
        :param type: field type of the field. Must be out of:
            - Numeric
            - Date
            - SingleLine
            - ComboBoxEntry
            - MultiLine
            - CheckBox
            - Calculation

        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return instance of the sample class

        """

        if not name:
            raise ValueError("Name cannot be empty")

        if not type ["Numeric", "Date", "SingleLine", "ComboBoxEntry", "MultiLine", "CheckBox", "Calculation"]:
            raise ValueError("type must be one of Numeric, Date, SingleLine, ComboBoxEntry, MultiLine, CheckBox, Calculation")

        data = {"name": name, "type": type}
        id = cls.post(data, project_id)
        data["id"] = id
        return data

    @classmethod
    @BaseClass._create_instances_decorator
    def create_many(cls, data_list: List[Dict], project_id=None) -> Self:
        """
        Method to create multiple samples

        :param data_list: dict with the following keys:
        - name: the name of the field to be created
        - type: field type of the field. Must be out of:
            - Numeric
            - Date
            - SingleLine
            - ComboBoxEntry
            - MultiLine
            - CheckBox
            - Calculation

        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return list with instance of the sample class
        """

        for data in data_list:
            if not "name" in data:
                raise ValueError("Name cannot be empty")

            if not data.get("type") in ["Numeric", "Date", "SingleLine", "ComboBoxEntry", "MultiLine", "CheckBox", "Calculation"]:
                raise ValueError(
                    "type must be one of Numeric, Date, SingleLine, ComboBoxEntry, MultiLine, CheckBox, Calculation")

        id_list = cls.post(data_list, project_id)
        for data, id in zip(data_list, id_list):
            data["id"] = id
        return data_list
