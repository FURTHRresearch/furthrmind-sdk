from ..utils import furthr_wrap
from furthrmind.collection.baseclass import (BaseClassWithFieldData, BaseClassWithFiles,
                                             BaseClassWithGroup, BaseClass,
                                             BaseClassWithLinking)
from typing_extensions import List, Dict, Self, TYPE_CHECKING
from inspect import isclass

if TYPE_CHECKING:
    from furthrmind.collection import *

class ResearchItem(BaseClassWithFieldData, BaseClassWithFiles, BaseClassWithGroup, BaseClassWithLinking, BaseClass ):
    id = ""
    name = ""
    neglect = False
    shortid = ""
    files: List["File"] = []
    fielddata: List["FieldData"] = []
    linked_experiments: List["Experiment"] = []
    linked_samples: List["Sample"] = []
    linked_researchitems: Dict[str, List["ResearchItem"]] = {}
    groups: List["Group"] = []
    category: "Category" = None
    datatables: List["DataTable"] = []

    _attr_definition = {
        "files": {"class": "File"},
        "fielddata": {"class": "FieldData"},
        "groups": {"class": "Group"},
        "linked_samples": {"class": "Sample"},
        "linked_experiments": {"class": "Experiment"},
        "linked_researchitems": {"class": "ResearchItem", "nested_dict": True},
        "datatables": {"class": "DataTable"},
        "category": {"class": "Category"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def _get_url_instance(self, project_id=None):
        project_url = ResearchItem.fm.get_project_url(project_id)
        url = f"{project_url}/researchitems/{self.id}"
        return url

    @classmethod
    def _get_url_class(cls, id, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchitems/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchitems"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchitems"
        return url
    
    @classmethod
    def get(cls, id: str = "", shortid: str = "", name: str = "", category_name: str = "", category_id: str = "",
            project_id: str = "") -> Self:
        """
        Method to get  one researchitem by its id, short_id or name. If requested by name, also category_name or
        category_id is required.
        If called on an instance of the class, the id of the class is used

        Parameters
        ----------
        id : str, optional
            The id of the requested research item.

        shortid : str, optional
            The short id of the requested research item.

        name : str, optional
            The name of the requested research item.

        category_name : str, optional
            The name of the category the research item belongs to.

        category_id : str, optional
            The id of the category the research item belongs to.

        project_id : str, optional
            Optionally to get a researchitem from another project as the furthrmind sdk was initiated with

        Returns
        -------
        Self
            Instance of the researchitem class.

        Raises
        ------
        AssertionError
            If used as a class method and neither id, shortid, nor name is provided.
            If used as a class method and name is provided but neither category_name nor category_id is provided.

        """

        if isclass(cls):
            assert id or shortid or name, AssertionError("Either id, shortid or name must be given")
            if not id and name:
                assert category_name or category_id, AssertionError("Either category name or id must be given")

        return cls._get(id=id, shortid=shortid, name=name,
                        category_name=category_name, category_id=category_id, project_id=project_id)


    @classmethod
    def get_many(cls, ids: List[str] = (), shortids: List[str] = (), names: List[str] = (),
                 category_name=None, category_id=None, project_id=None) -> List[Self]:
        """
        Method to get many researchitems by ids or shortids. If requested by names, also category_name or category_id
        is required. If requested by name items from one category can be requested at a time.

        Parameters
        ----------
        ids : List[str]
             List of experiment ids.
        shortids : List[str]
             List of experiment short ids.
        names : List[str]
             List of experiment names.
        category_name : str, optional
             Name of the category the research item belongs to.
        category_id : str, optional
             Id of the category the research item belongs to.
        project_id : str, optional
             Optionally to get researchitems from another project as the furthrmind sdk was initiated with

        Returns
        -------
        List[Self]
             List of instances of the researchitem class.

        Raises
        ------
        AssertionError
            ids, shortids, nor names must be provided.
            If names is provided but neither category_name nor category_id is provided.

        """

        assert ids or shortids or names, AssertionError("Either ids, shortids or names must be given")
        if names:
            assert category_name or category_id, AssertionError("Either category_name or category_id must be given")

        return cls._get_many(ids, shortids, names, category_name, category_id, project_id=project_id)

    @classmethod
    def get_all(cls, project_id: str = "") -> List[Self]:
        """
        Method to get all researchitems belonging to one project

        Parameters
        ----------
        project_id: str
            Optionally to get researchitems from another project as the furthrmind sdk was initiated with

        Returns
        -------
        List[Self]
            A list containing instances of the researchitem class.
        """

        return cls._get_all(project_id)


    @classmethod
    @BaseClass._create_instances_decorator(_fetched=False)
    def create(cls, name: str, group_name: str = "", group_id: str = "", category_name: str = "", category_id: str = "",
               project_id=None) -> Self:
        """
        Parameters
        ----------
        name : str
            The name of the item to be created.
        group_name : str, optional
            The name of the group where the new item will belong to. Group name can only be considered for groups that
            are not subgroups. Either `group_name` or `group_id` must be specified.
        group_id : str, optional
            The id of the group where the new item will belong to. Either `group_name` or `group_id` must be specified.
        category_name : str, optional
            The name of the category that the new item will belong to. Either `category_name` or `category_id` must be specified.
        category_id : str, optional
            The id of the category that the new item will belong to. Either `category_name` or `category_id` must be specified.
        project_id : object, optional
            Optionally create a researchitem in another project as the furthrmind sdk was initiated with.

        Returns
        -------
        Self
            instance of the researchitem class

        Raises
        ------
        AssertationError
            If neither group_id nor group_name is provided.
            If neither `category_name` nor `category_id` are specified.

        """

        from furthrmind.collection import Category

        assert group_name or group_id, "Either group_name or group_id must be specified"
        assert category_name or category_id, "Either category name or id must be specified"

        data = cls._prepare_data_for_create(name, group_name, group_id, project_id)

        category_dict = {}
        if category_name:
            category_dict["name"] = category_name
        if category_id:
            category_dict["id"] = category_id

        data["category"] = category_dict
        id = cls._post(data, project_id)

        if "id" not in category_dict:
            categories = Category._get_all(project_id)
            for cat in categories:
                if cat.name == category_name:
                    category_dict["id"] = cat.id
                    break

        data["id"] = id
        return data

    @classmethod
    @BaseClass._create_instances_decorator(_fetched=False)
    def create_many(cls, data_list: List[Dict], project_id: str = "") -> Self:
        """
        Parameters
        ----------
        data_list : List[Dict]
            List of dictionaries containing information about the items to be created. Each dictionary should have the
            following keys:
                - name: str
                    The name of the group to be created.
                - group_name: str
                    The name of the group where the new item will belong to. Group name can only be considered for groups
                    that are not subgroups. Either group_name or group_id must be specified.
                - group_id: int or None
                    The ID of the group where the new item will belong to. Either group_name or group_id must be specified.
                - category_name: str
                    The name of the category that the new item will belong to. Either category_name or category_id must be specified.
                - category_id: int or None
                    The ID of the category that the new item will belong to. Either category_name or category_id must be specified.
        project_id : str, optional
            Optionally to create researchitems in another project as the furthrmind sdk was initiated with

        Returns
        -------
        List[Self]
            A list of instances of the researchitem class created.

        Raises
        ------
        AssertationError
            If name not specified
            If neither category name nor ID is specified.
            If neither group_id nor group_name is provided.


        """

        new_list = []
        category_id_not_present = False

        for data in data_list:
            category_name = data.get('category_name')
            category_id = data.get('category_id')
            assert category_name or category_id, "Either category name or id must be specified"

            # raises an error if name not specified or if neither group_name nor group_id is provided
            temp_data = cls._prepare_data_for_create(data.get("name"), data.get("group_name"), data.get("group_id"),
                                                     project_id)

            category_dict = {}
            if category_name:
                category_dict["name"] = category_name
            if category_id:
                category_dict["id"] = category_id

            temp_data["category"] = category_dict
            new_list.append(temp_data)
            if not "id" in category_dict:
                category_id_not_present = True

        id_list = cls._post(new_list, project_id)
        category_mapping = {}
        if category_id_not_present:
            categories = Category._get_all(project_id)
            category_mapping = {cat.name: cat for cat in categories}

        for data, id in zip(new_list, id_list):
            data["id"] = id
            if "id" not in data["category"]:
                cat_id = category_mapping.get(data["category"]["name"])
                data["category"]["id"] = cat_id

        return new_list

    def add_datatable(self, name: str, columns: List[Dict], project_id: str = "" ) -> "DataTable":
        """
        Method to create a new datatable within this researchitem. Add the created datatable to the datatables attribute

        Parameters
        ----------
        name : str
            Name of the datatable.
        columns : List[Dict]
            A list of columns that should be added to the datatable. Each column is represented as a dictionary with the following keys:
            - name : str
                Name of the column.
            - type : str
                Type of the column. Either "Text" or "Numeric". Data must fit the specified type.
            - data : Union[List[Union[str, float]], pandas.Series]
                List of column values. Data must fit the specified type of the column.
                For Text columns, the items must be convertable to strings
                For Numeric columns, the items must be convertable to floats.
                Can be a list or a pandas.Series.
            - unit : dict or str
                Unit of the column. It can be represented as either a dictionary with 'id' or 'name', or a string
                representing the name or id of the unit.
        project_id : str, optional
            Optionally, specify the id of another project to create the datatable in.

        Returns
        -------
        DataTable
            An instance of the DataTable class representing the created datatable.

        """

        from furthrmind.collection import DataTable
        datatable = DataTable.create(name, researchitem_id=self.id, columns=columns, project_id=project_id)

        new_datatable = list(self.datatables)
        new_datatable.append(datatable)
        self.datatables = new_datatable

        return datatable

