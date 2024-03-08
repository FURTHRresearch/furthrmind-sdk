from functools import wraps
from furthrmind_sdk.utils import furthr_wrap, instance_overload

class BaseClass:
    _data = {}
    _fetched = False
    _id = None
    fm = None

    attr_definition = {}

    def __init__(self, id=None, data=None):
        if data:
            self._update_attributes(data)

        if id:
            self._id = id
        else:
            if "id" in self._data:
                self._id = self._data["id"]
        if not self._id:
            raise ValueError("No id provided")

        # create instance methods for certain class_methods
        instance_methods = ["get", "get_all"]
        instance_overload(self, instance_methods)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            raise ValueError("No such attribute")

    @staticmethod
    def _get_url(id=None, project_id=None):
        return ""

    @classmethod
    def _get_all_url(cls, project_id=None):
        return ""

    @classmethod
    def _post_url(cls, project_id=None):
        return ""

    @staticmethod
    def update_instance_decorator(f):
        @wraps(f)
        def decorated(*args, **kws):
            self = args[0]
            self._update_attributes(*args, **kws)

        return decorated

    @staticmethod
    def create_instances_decorator(f):
        @wraps(f)
        def decorated(*args, **kws):
            results = f(*args, **kws)
            if issubclass(args[0], BaseClass):
                cls = args[0]
            else:
                self = args[0]
                cls = self.__class__
            item_list = []
            for r in results:
                item = cls(data=r)
                item_list.append(item)
            return item_list

        return decorated

    def _update_attributes(self, data):
        from furthrmind_sdk.collection import get_collection_class
        self._data = data

        def _create_instance(classname, _data):
            cls = get_collection_class(classname)
            if isinstance(_data, list):
                item_list = []
                for item in data[key]:
                    item = cls(self.fm, data=item)
                    item_list.append(item)
                item = item_list
            else:
                item = cls(self.fm, data=_data)
            return item

        for key in data:
            if hasattr(self, key):
                item = data[key]
                if key in self.attr_definition:
                    attr_definition = self.attr_definition[key]
                    if "class" in attr_definition:
                        if "nested_dict" in attr_definition:
                            item = {}
                            for item_key in data[key]:
                                item[item_key] = _create_instance(attr_definition["class"],
                                                                  data[key][item_key])
                        else:
                            item = _create_instance(attr_definition["class"], data[key])

                setattr(self, key, item)
            else:
                for attr_definition in self.attr_definition.items():
                    definition_key = attr_definition[0]
                    definition_value = attr_definition[1]
                    if "data_key" in definition_value:
                        if definition_value["data_key"] == key:
                            item = data["data_key"]
                            if "class" in definition_value:
                                item = _create_instance(definition_value["class"], data[key])
                            setattr(self, definition_key, item)
                            break

    @classmethod
    def get(cls, id=None):
        if issubclass(cls, BaseClass):
            return cls._get_class_method(id)
        else:
            self = cls
            return self._get_instance_method()

    @update_instance_decorator
    @furthr_wrap
    def _get_instance_method(self):
        url = self._get_url()
        return self.fm.session.get(url)

    @classmethod
    @update_instance_decorator
    @furthr_wrap
    def _get_class_method(cls, id):
        url = cls._get_url(id)
        return cls.fm.session.get(url)

    @classmethod
    def get_all(cls, project_id=None):
        if issubclass(cls, BaseClass):
            return cls._get_all_class_method(project_id)
        else:
            cls = cls.__class__
            return cls._get_all_class_method(project_id)

    @classmethod
    @create_instances_decorator
    @furthr_wrap
    def _get_all_class_method(cls, project_id):
        from .project import Project
        if cls in [Project]:
            url = cls._get_all_url()
        else:
            url = cls._get_url(project_id)
        return BaseClass.fm.session.get(url)

    @furthr_wrap
    def _post_method(self, data):
        url = self._post_url()
        return self.fm.session.post(url, json=data)


class BaseClassWithFieldData(BaseClass):
    fielddata = []

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def update_field_value(self, value, fieldname=None, fieldid=None):
        """
        :param value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        :param fieldname: Name of field that should be updated. Either field_name or field_id must be specified
        :param fieldid: id of field that should be updated. Either field_name or field_id must be specified
        :return: id
        """
        fielddata = None
        for fielddata in self.fielddata:
            if fieldid:
                if fielddata.fieldid == fieldid:
                    fielddata= fielddata
            elif fieldname:
                if fielddata.field_name == fieldname:
                    fielddata = fielddata

        if not fielddata:
            raise ValueError("No field found with the given fieldid or fieldname")

        return fielddata.update_value(value)

    def add_field(self, fieldname=None, fieldtype=None, fieldid=None,
                  value=None, unit=None):
        """

        :param fieldname: Name of field that should be updated. If fieldname provided,
                            also fieldtype must be specified. Either fieldname and fieldtype or field_id must be specified
        :param fieldtype: Type of field: Must be out of: Numeric, Date, SingleLine
                                                        ComboBoxEntry, MultiLine, CheckBox
        :param fieldid: id of field that should be added.
        :param value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        :param unit: dict with id or name, or name as string, or id as string
        :return: id
        """
        from .fielddata import FieldData
        from .field import Field
        if fieldid:
            data = {"fieldid": fieldid}
            field = Field(id=fieldid)
            field.get()
            fieldtype = field.type
        else:
            if not fieldname or not fieldtype:
                raise ValueError("fieldname and fieldtype must be specified")
            data = {"fieldname": fieldname,
                    "fieldtype": fieldtype}

        value = FieldData._check_value_type(value, fieldtype)
        data["value"] = value

        if unit:
            unit = FieldData._check_unit(unit)
            data["unit"] = unit

        id = self._post_method(data)
