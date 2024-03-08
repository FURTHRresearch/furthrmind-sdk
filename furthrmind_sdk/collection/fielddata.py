from ..utils import furthr_wrap
from functools import wraps
from furthrmind_sdk.collection.baseclass import BaseClass
from datetime import datetime, date
from bson import ObjectId
from furthrmind_sdk.utils import instance_overload

class FieldData(BaseClass):
    id = ""
    fieldname = ""
    fieldid = ""
    fieldtype = ""
    si_value = None
    unit = None
    author = None
    value = None


    attr_definition = {
        "unit": {"class": "Unit"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

        # create instance methods for certain class_methods
        instance_methods = ["_check_value_type"]
        instance_overload(self, instance_methods)

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/fielddata"
        return url

    @classmethod
    def get(cls, id=None):
        raise TypeError("Not implemented")

    @classmethod
    def get_all(cls, project_id=None):
        raise TypeError("Not implemented")

    def update_value(self, value):
        """
        :param value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        :return: id
        """
        value = self._check_value_type(value)
        data = {"id": self.id,
                "value": value}
        id = self._post_method(data)
        self.value = value
        return id

    @classmethod
    def _check_value_type(cls, value, fieldtype=None):
        if issubclass(cls, BaseClass):
            # classmethod
            if fieldtype is None:
                raise ValueError("fieldtype must not be None")
        else:
            # instance method
            self = cls
            fieldtype = self.fieldtype
        if fieldtype == "Numeric":
            try:
                value = float(value)
            except:
                raise TypeError("Not numeric")
            return value
        elif fieldtype == "Date":
            if isinstance(value, datetime):
                return int(value.timestamp())
            if isinstance(value, date):
                value = datetime.combine(value, datetime.min.time())
                return int(value.timestamp())
            if isinstance(value, str):
                try:
                    value = datetime.fromisoformat(value)
                    return int(value.timestamp())
                except ValueError:
                    raise TypeError("No iso time format")
            if isinstance(value, int):
                return value
        elif fieldtype == "SingleLine":
            if isinstance(value, str):
                return value
            if isinstance(value, (float, int)):
                return str(value)
            raise TypeError("Type must be string")

        elif fieldtype == "ComboBoxEntry":
            if isinstance(value, dict):
                if "id" in value:
                    return value
                if "name" in value:
                    return value
                raise TypeError("The dict must have either id or name key")
            if isinstance(value, str):
                try:
                    value = ObjectId(value)
                    value = {"id": value}
                except:
                    value = {"name": value}
                return value
            raise TypeError("Only string and dict supported")

        elif fieldtype == "MultiLine":
            if isinstance(value, dict):
                if "content" not in value:
                    raise TypeError("Key 'content' is required")
                return value
            if isinstance(value, str):
                value = {"content": value}
                return value
            raise TypeError("Only string and dict supported")

        elif fieldtype == "CheckBox":
            if not isinstance(value, bool):
                raise TypeError("value must be a bool")
            return value

    def update_unit(self, unit):
        """
        :param unit:
            - dict with id or name, or name as string, or id as string
        :return: id
        """
        unit = self._check_unit(unit)
        data = {"id": self.id,
                "unit": unit}
        id = self._post_method(data)
        self.unit = unit
        return id

    @classmethod
    def _check_unit(cls, unit):
        if not unit:
            return unit
        if isinstance(unit, dict):
            if "id" in unit:
                return unit
            if "name" in unit:
                return unit
            raise TypeError("The dict must have either id or name key")

        elif isinstance(unit, str):
            try:
                unit = ObjectId(unit)
                unit = {"id": unit}
            except:
                unit = {"name": unit}
            return unit
        raise TypeError("Only string and dict supported")

