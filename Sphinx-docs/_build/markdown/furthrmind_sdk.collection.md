# furthrmind_sdk.collection package

## Submodules

## furthrmind_sdk.collection.baseclass module

### *class* furthrmind_sdk.collection.baseclass.BaseClass(id=None, data=None)

Bases: `object`

#### \_\_init_\_(id=None, data=None)

#### fm *= None*

#### *classmethod* get(id=None)

#### *classmethod* get_all(project_id=None)

* **Return type:**
  `List`[`Self`]

#### *classmethod* post(data, project_id=None)

### *class* furthrmind_sdk.collection.baseclass.BaseClassWithFieldData(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### add_field(field_name=None, field_type=None, field_id=None, value=None, unit=None)

* **Parameters:**
  * **field_name** – Name of field that should be added. If fieldname provided,
    also fieldtype must be specified. Either fieldname and fieldtype or field_id must be specified
  * **field_type** – Type of field: Must be out of: Numeric, Date, SingleLine
    ComboBoxEntry, MultiLine, CheckBox
  * **field_id** – id of field that should be added.
  * **value** – 
    - Numeric: float or int, or a string convertable to a float
    - Date: datetime, or date object, or unix timestamp or string with iso format
    - SingleLine: string
    - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
    - MultiLine: dict with content as key, or string
    - CheckBox: boolean
  * **unit** – dict with id or name, or name as string, or id as string
* **Return type:**
  [`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)
* **Returns:**
  fielddata object

#### add_many_fields(data_list)

Method to add many fields to an item. Each field is defined by and dict in the data_list parameter

* **Parameters:**
  **data_list** (`List`[`Dict`]) – dict with the following key

- field_name: Name of field that should be added. If fieldname provided, also fieldtype must be specified. Either fieldname and fieldtype or field_id must be specified
- field_type: Type of field: Must be out of: Numeric, Date, SingleLine
  : ComboBoxEntry, MultiLine, CheckBox
- field_id: id of field that should be added.
- value:
  : - Numeric: float or int, or a string convertable to a float
    - Date: datetime, or date object, or unix timestamp or string with iso format
    - SingleLine: string
    - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
    - MultiLine: dict with content as key, or string
    - CheckBox: boolean
- unit: dict with id or name, or name as string, or id as string

* **Return type:**
  `List`[[`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)]
* **Returns:**
  list with fielddata object

#### fielddata *= []*

#### id *= None*

#### remove_field(fieldname=None, fieldid=None)

* **Parameters:**
  * **fieldname** – Name of field that should be removed. Either id or fieldname must be specified
  * **fieldid** – id of field that should be removed.

:return id of item

#### update_field_unit(unit, field_name=None, field_id=None)

* **Parameters:**
  * **value** – 
    - Numeric: float or int, or a string convertable to a float
    - Date: datetime, or date object, or unix timestamp or string with iso format
    - SingleLine: string
    - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
    - MultiLine: dict with content as key, or string
    - CheckBox: boolean
  * **field_name** – Name of field that should be updated. Either field_name or field_id must be specified
  * **field_id** – id of field that should be updated. Either field_name or field_id must be specified
* **Returns:**
  id

#### update_field_value(value, fieldname=None, fieldid=None)

* **Parameters:**
  * **value** – 
    - Numeric: float or int, or a string convertable to a float
    - Date: datetime, or date object, or unix timestamp or string with iso format
    - SingleLine: string
    - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
    - MultiLine: dict with content as key, or string
    - CheckBox: boolean
  * **field_name** – Name of field that should be updated. Either field_name or field_id must be specified
  * **field_id** – id of field that should be updated. Either field_name or field_id must be specified
* **Returns:**
  id

### *class* furthrmind_sdk.collection.baseclass.BaseClassWithFiles(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### add_file(file_path, file_name=None)

* **Parameters:**
  * **file_path** – file path of the file that should be uploaded
  * **file_name** – Optionally specify the file name if not the original file name should be used
* **Return type:**
  [`File`](#furthrmind_sdk.collection.file.File)
* **Returns:**
  file object

#### files *= []*

#### id *= None*

#### remove_file(file_id=None, file_name=None)

* **Parameters:**
  * **file_id** – id of file that should be removed, either file_name or file_id must be specified
  * **file_name** – file name of file to be removed
* **Returns:**
  file object

### *class* furthrmind_sdk.collection.baseclass.BaseClassWithGroup(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### groups *= []*

#### id *= None*

## furthrmind_sdk.collection.category module

### *class* furthrmind_sdk.collection.category.Category(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### *static* create()

#### description *= ''*

#### *classmethod* get(id=None)

Method to get all one category by it’s id
If called on an instance of the class, the id of the class is used
:param str id: id of requested category 
:return Self: Instance of category class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all categories belonging to one project
:param str project_id: Optionally to get categories from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of category class

* **Return type:**
  `List`[`Self`]

#### id *= ''*

#### name *= ''*

#### project *= ''*

## furthrmind_sdk.collection.column module

### *class* furthrmind_sdk.collection.column.Column(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### *classmethod* create(cls, name, type, data, unit=None, project_id=None)

Method to create a new data column

* **Parameters:**
  * **name** (`str`) – Name of the column
  * **type** (`str`) – Type of the column, Either “Text” or “Numeric”. Data must fit to type, for Text all data
    will be converted to string and for Numeric all data is converted to float (if possible)
  * **data** (`list`) – List of column values, must fit to column_type
  * **unit** – dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  Instance of column class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create a new data column

* **Parameters:**
  * **data_list** (`List`[`Dict`]) – dict with the following keys:
    - name: Name of the column
    - type: Type of the column, Either “Text” or “Numeric”. Data must fit to type, for Text all data
    will be converted to string and for Numeric all data is converted to float (if possible)
    - data: List of column values, must fit to column_type
    - unit: dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  List with instances of column class

#### *classmethod* get(id=None)

Method to get all one column by it’s id
If called on an instance of the class, the id of the class is used
:param str id: id of requested column 
:return Self: Instance of column class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

* **Return type:**
  `List`[`Self`]

#### *classmethod* get_many(cls, id_list, project_id=None)

Method to get many columns

* **Parameters:**
  * **id_list** – list of column ids that should be retrieved
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `List`[`Self`]
* **Returns:**
  list of column objects

#### id *= ''*

#### name *= ''*

#### type *= ''*

#### values *= []*

## furthrmind_sdk.collection.comboboxentry module

### *class* furthrmind_sdk.collection.comboboxentry.ComboBoxEntry(id=None, data=None)

Bases: [`BaseClassWithFieldData`](#furthrmind_sdk.collection.baseclass.BaseClassWithFieldData)

#### \_\_init_\_(id=None, data=None)

#### *classmethod* create(cls, name, field_name=None, field_id=None, project_id=None)

Method to create a new combobox entry

* **Parameters:**
  * **name** (`str`) – name of the combobox entry
  * **field_name** (`Optional`[`str`]) – Name of the field, where the combobox entry should belong to. Either the field name or id
    must be provided
  * **field_id** – id of the field, where the combobox entry should belong to. Either the field name or id must
    be provided
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  instance of column comboboxentry class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create a new data column

* **Parameters:**
  * **data_list** (`List`[`Dict`]) – dict with the following keys:
    - name of the combobox entry
    - field_name: Name of the field, where the combobox entry should belong to. Either the field name or id
    must be provided
    - field_id: id of the field, where the combobox entry should belong to. Either the field name or id must
    be provided
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  List with instances of comboboxentry class

#### fielddata *: `List`[[`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)]* *= []*

#### files *: `List`[[`File`](#furthrmind_sdk.collection.file.File)]* *= []*

#### *classmethod* get(id=None)

Method to get all one comboboxentry by it’s id
If called on an instance of the class, the id of the class is used
:param str id: id of requested comboboxentry 
:return Self: Instance of comboboxentry class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all comboboxentries belonging to one project
:param str project_id: Optionally to get comboboxentries from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of comboboxentry class

* **Return type:**
  `List`[`Self`]

#### id *= ''*

#### name *= ''*

## furthrmind_sdk.collection.datatable module

### *class* furthrmind_sdk.collection.datatable.DataTable(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### columns *: `List`[[`Column`](#furthrmind_sdk.collection.column.Column)]* *= []*

#### *classmethod* create(cls, name='Data table', experiment_id=None, sample_id=None, researchitem_id=None, columns=None, project_id=None)

Method to create a new datatable

* **Parameters:**
  * **name** (`str`) – name of the datatable
  * **experiment_id** – id of the experiment where the datatable belongs to
  * **sample_id** – id of the sample where the datatable belongs to
  * **researchitem_id** – id of the researchitem where the datatable belongs to
  * **columns** – a list of columns that should be added to the datatable. List with dicts with the following keys:
    - name: name of the column
    - type: Type of the column, Either “Text” or “Numeric”. Data must fit to type, for Text all data
    will be converted to string and for Numeric all data is converted to float (if possible)
    - data: List of column values, must fit to column_type
    - unit: dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  instance of datatable class

#### *classmethod* get(id=None)

Method to get all one datatable by it’s id
If called on an instance of the class, the id of the class is used
:param str id: id of requested datatable 
:return Self: Instance of datatable class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all datatables belonging to one project
:param str project_id: Optionally to get datatables from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of datatable class

* **Return type:**
  `List`[`Self`]

#### get_columns(column_id_list=None, column_name_list=None)

Method to get columns and their data
If column_id_list and column_name_list are not provided, the method will retrieve all columns belonging
to the datatable

* **Parameters:**
  * **column_id_list** (`Optional`[`List`[`str`]]) – list of column_ids to retrieve
  * **column_name_list** (`Optional`[`List`[`str`]]) – list of column names to retrieve
* **Return type:**
  `List`[[`Column`](#furthrmind_sdk.collection.column.Column)]
* **Returns:**
  list of column objects

#### get_pandas_dataframe(column_id_list=None, column_name_list=None)

Method to get columns and their data as a pandas dataframe
If column_id_list and column_name_list are not provided, the method will retrieve all columns belonging
to the datatable

* **Parameters:**
  * **column_id_list** (`Optional`[`List`[`str`]]) – list of column_ids to retrieve
  * **column_name_list** (`Optional`[`List`[`str`]]) – list of column names to retrieve
* **Return type:**
  `DataFrame`
* **Returns:**
  pandas dataframe

#### id *= ''*

#### name *= ''*

## furthrmind_sdk.collection.experiment module

### *class* furthrmind_sdk.collection.experiment.Experiment(id=None, data=None)

Bases: [`BaseClassWithFieldData`](#furthrmind_sdk.collection.baseclass.BaseClassWithFieldData), [`BaseClassWithFiles`](#furthrmind_sdk.collection.baseclass.BaseClassWithFiles), [`BaseClassWithGroup`](#furthrmind_sdk.collection.baseclass.BaseClassWithGroup)

#### \_\_init_\_(id=None, data=None)

#### add_datatable(name, columns, project_id=None)

Method to create a new datatable within this experiment

* **Parameters:**
  * **name** (`str`) – name of the datatable
  * **columns** (`List`[`Dict`]) – a list of columns that should be added to the datatable. List with dicts with the following keys:
    - name: name of the column
    - type: Type of the column, Either “Text” or “Numeric”. Data must fit to type, for Text all data
    will be converted to string and for Numeric all data is converted to float (if possible)
    - data: List of column values, must fit to column_type
    - unit: dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  [`DataTable`](#furthrmind_sdk.collection.datatable.DataTable)
* **Returns:**
  instance of column datatable class

#### *classmethod* create(cls, name, group_name=None, group_id=None, project_id=None)

Method to create a new experiment

* **Parameters:**
  * **name** – the name of the item to be created
  * **group_name** – The name of the group where the new item will belong to. group name can be only considered
    for groups that are not subgroups. Either group_name or group_id must be specified
  * **group_id** – the id of the group where the new item will belong to. Either group_name or group_id must be specified
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`

:return instance of the experiment class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create multiple experiments

* **Parameters:**
  * **data_list** (`List`[`Dict`]) – dict with the following keys:
    - name: the name of the item to be created
    - group_name: The name of the group where the new item will belong to. group name can be only considered
    for groups that are not subgroups. Either group_name or group_id must be specified
    - group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`

:return list with instance of the experiment class

#### datatables *: `List`[[`DataTable`](#furthrmind_sdk.collection.datatable.DataTable)]* *= []*

#### fielddata *: `List`[[`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)]* *= []*

#### files *: `List`[[`File`](#furthrmind_sdk.collection.file.File)]* *= []*

#### *classmethod* get(id=None, name=None)

Method to get all one experiment by it’s id or short_id
If called on an instance of the class, the id of the class is used
:param str id: id or short_id of requested experiment 
:param str name: name of requested experiment 
:return Self: Instance of experiment class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all experiment belonging to one project
:param str project_id: Optionally to get experiments from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of experiment class

* **Return type:**
  `List`[`Self`]

#### groups *: `List`[[`Group`](#furthrmind_sdk.collection.group.Group)]* *= []*

#### id *= ''*

#### linked_experiments *: `List`[`Self`]* *= []*

#### linked_researchitems *: `Dict`[`str`, `List`[[`ResearchItem`](#furthrmind_sdk.collection.researchitem.ResearchItem)]]* *= []*

#### linked_samples *: `List`[[`Sample`](#furthrmind_sdk.collection.sample.Sample)]* *= []*

#### name *= ''*

#### neglect *= False*

#### shortid *= ''*

## furthrmind_sdk.collection.field module

### *class* furthrmind_sdk.collection.field.Field(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### comboboxentries *: `List`[[`ComboBoxEntry`](#furthrmind_sdk.collection.comboboxentry.ComboBoxEntry)]* *= []*

#### *classmethod* create(cls, name, type, project_id=None)

Method to create a new sample

* **Parameters:**
  * **name** – the name of the field to be created
  * **type** – field type of the field. Must be out of:
    - Numeric
    - Date
    - SingleLine
    - ComboBoxEntry
    - MultiLine
    - CheckBox
    - Calculation
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`

:return instance of the sample class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create multiple samples
:rtype: `Self`

* **Parameters:**
  **data_list** (`List`[`Dict`]) – dict with the following keys:

- name: the name of the field to be created
- type: field type of the field. Must be out of:
  : - Numeric
    - Date
    - SingleLine
    - ComboBoxEntry
    - MultiLine
    - CheckBox
    - Calculation

* **Parameters:**
  **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with

:return list with instance of the sample class

#### *classmethod* get(id=None, name=None)

Method to get all one field by it’s id
:param str id: id of requested field 
:param str name: name of requested field 
:return Self: Instance of field class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all fields belonging to one project
If called on an instance of the class, the id of the class is used
:param str project_id: Optionally to get fields from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of field class

* **Return type:**
  `List`[`Self`]

#### id *= ''*

#### name *= ''*

#### script *= ''*

#### type *= ''*

## furthrmind_sdk.collection.fielddata module

### *class* furthrmind_sdk.collection.fielddata.FieldData(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### author *= None*

#### *classmethod* create(field_name, field_type, field_id, value, unit, project_id=None)

Method to create a new fielddata

* **Parameters:**
  * **field_name** – name of the field. Either field name and field_type must be specified, or field_id
    must be specified
  * **field_type** – type of the field. Must be out of:
    - Numeric
    - Date
    - SingleLine
    - ComboBoxEntry
    - MultiLine
    - CheckBox
    - Calculation
  * **field_id** – id of the field
  * **value** – 
    - Numeric: float or int, or a string convertable to a float
    - Date: datetime, or date object, or unix timestamp or string with iso format
    - SingleLine: string
    - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
    - MultiLine: dict with content as key, or string
    - CheckBox: boolean
  * **unit** – dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Returns:**
  instance of fielddata class

#### *classmethod* create_many(data_list, project_id=None)

Method to create many new fielddata

* **Parameters:**
  **data_list** – List with dicts with the following kneys:

- field_name: name of the field. Either field name and field_type must be specified, or field_id
  : must be specified
- field_type: type of the field. Must be out of:
  : - Numeric
    - Date
    - SingleLine
    - ComboBoxEntry
    - MultiLine
    - CheckBox
    - Calculation
- field_id: id of the field
- value:
  : - Numeric: float or int, or a string convertable to a float
    - Date: datetime, or date object, or unix timestamp or string with iso format
    - SingleLine: string
    - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
    - MultiLine: dict with content as key, or string
    - CheckBox: boolean
- unit: dict with id or name, or name as string, or id as string

* **Parameters:**
  **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Returns:**
  list with instances of fielddata class

#### field_id *= ''*

#### field_name *= ''*

#### field_type *= ''*

#### *classmethod* get(id=None)

#### *classmethod* get_all(project_id=None)

#### id *= ''*

#### si_value *= None*

#### unit *: `List`[[`Unit`](#furthrmind_sdk.collection.unit.Unit)]* *= None*

#### update_unit(unit)

Method to update the unit of fielddata

* **Parameters:**
  **unit** – 
  - dict with id or name, or name as string, or id as string
* **Returns:**
  id

#### update_value(value)

Method to update the value of fielddata

* **Parameters:**
  **value** – 
  - Numeric: float or int, or a string convertable to a float
  - Date: datetime, or date object, or unix timestamp or string with iso format
  - SingleLine: string
  - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
  - MultiLine: dict with content as key, or string
  - CheckBox: boolean
* **Returns:**
  id

#### value *= None*

## furthrmind_sdk.collection.file module

### *class* furthrmind_sdk.collection.file.File(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### download(folder, overwrite=False)

Method to download a file
:type folder: 
:param folder: the folder where the file should be saved

#### download_bytes()

Method to download a file and save to BytesIO object
:param folder: the folder where the file should be saved

* **Return type:**
  `BytesIO`

#### *classmethod* get(id=None)

#### *classmethod* get_all()

#### id *= ''*

#### name *= ''*

#### update_file(file_path, file_name=None)

## furthrmind_sdk.collection.group module

### *class* furthrmind_sdk.collection.group.Group(id=None, data=None)

Bases: [`BaseClassWithFieldData`](#furthrmind_sdk.collection.baseclass.BaseClassWithFieldData)

#### \_\_init_\_(id=None, data=None)

#### *classmethod* create(cls, name, project_id=None)

Method to create a new sample
:type name: 
:param name: the name of the item to be created
:type project_id: 
:param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
:return instance of the group class

* **Return type:**
  `Self`

#### *classmethod* create_many(cls, name_list, project_id=None)

Method to create multiple groups
:type name_list: `List`[`str`]
:param name_list: list with names of the groups to be created
:type project_id: 
:param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
:return list with instance of the group class

* **Return type:**
  `List`[`Self`]

#### experiments *: `List`* *= []*

#### fielddata *: `List`[[`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)]* *= []*

#### files *: `List`[[`File`](#furthrmind_sdk.collection.file.File)]* *= []*

#### *classmethod* get(id=None, name=None)

Method to get all one group by it’s id or short_id
If called on an instance of the class, the id of the class is used
:param str id: id or short_id of requested group 
:param str name: name of requested group 
:return Self: Instance of group class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all groups belonging to one project
:param str project_id: Optionally to get groups from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of group class

* **Return type:**
  `List`[`Self`]

#### id *= ''*

#### name *= ''*

#### neglect *= False*

#### parent_group *: `Self`* *= None*

#### researchitems *: `Dict`[`str`, `List`[[`ResearchItem`](#furthrmind_sdk.collection.researchitem.ResearchItem)]]* *= {}*

#### samples *: `List`[[`Sample`](#furthrmind_sdk.collection.sample.Sample)]* *= []*

#### shortid *= ''*

#### sub_groups *: `List`[`Self`]* *= []*

## furthrmind_sdk.collection.import_collection module

## furthrmind_sdk.collection.project module

### *class* furthrmind_sdk.collection.project.Project(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### *classmethod* create(cls, name)

Method to create a new project
:type name: `str`
:param name: Name of the new project
:rtype: `Self`
:return: instance of the project class

#### experiments *: `List`[[`Experiment`](#furthrmind_sdk.collection.experiment.Experiment)]* *= []*

#### fields *: `List`[[`Field`](#furthrmind_sdk.collection.field.Field)]* *= []*

#### *classmethod* get(id=None, name=None)

Method to get all one project by it’s id
If called on an instance of the class, the id of the class is used
:param str id: id or short_id of requested project 
:param str name: name of requested project 
:return Self: Instance of project class

* **Return type:**
  `Self`

#### *classmethod* get_all()

Method to get all projects belonging to one project
:return List[Self]: List with instances of project class

* **Return type:**
  `List`[`Self`]

#### groups *: `List`[[`Group`](#furthrmind_sdk.collection.group.Group)]* *= []*

#### id *= ''*

#### info *= ''*

#### name *= ''*

#### permissions *= []*

#### researchitems *: `Dict`[`str`, `List`[[`ResearchItem`](#furthrmind_sdk.collection.researchitem.ResearchItem)]]* *= {}*

#### samples *: `List`[[`Sample`](#furthrmind_sdk.collection.sample.Sample)]* *= []*

#### shortid *= ''*

#### units *: `List`[[`Unit`](#furthrmind_sdk.collection.unit.Unit)]* *= []*

## furthrmind_sdk.collection.researchitem module

### *class* furthrmind_sdk.collection.researchitem.ResearchItem(id=None, data=None)

Bases: [`BaseClassWithFieldData`](#furthrmind_sdk.collection.baseclass.BaseClassWithFieldData), [`BaseClassWithFiles`](#furthrmind_sdk.collection.baseclass.BaseClassWithFiles), [`BaseClassWithGroup`](#furthrmind_sdk.collection.baseclass.BaseClassWithGroup), [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### add_datatable(name, columns, project_id=None)

Method to create a new datatable within this experiment

* **Parameters:**
  * **name** (`str`) – name of the datatable
  * **columns** (`List`[`Dict`]) – a list of columns that should be added to the datatable. List with dicts with the following keys:
    - name: name of the column
    - type: Type of the column, Either “Text” or “Numeric”. Data must fit to type, for Text all data
    will be converted to string and for Numeric all data is converted to float (if possible)
    - data: List of column values, must fit to column_type
    - unit: dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  [`DataTable`](#furthrmind_sdk.collection.datatable.DataTable)
* **Returns:**
  instance of column datatable class

#### category *: [`Category`](#furthrmind_sdk.collection.category.Category)* *= None*

#### *classmethod* create(cls, name, group_name=None, group_id=None, category_name=None, category_id=None, project_id=None)

Method to create a new researchitem

* **Parameters:**
  * **name** – the name of the item to be created
  * **group_name** – The name of the group where the new item will belong to. group name can be only considered
    for groups that are not subgroups. Either group_name or group_id must be specified
  * **group_id** – the id of the group where the new item will belong to. Either group_name or group_id must be specified
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Category_name:**
  the name of the category that the new item will belong to. Either category_name or category_id must be specified
* **Return type:**
  `Self`
* **Category_id:**
  the id of the category that the new item will belong to. Either category_name or category_id must be specified

:return instance of the researchitem class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create multiple experiments

* **Parameters:**
  * **data_list** (`List`[`Dict`]) – dict with the following keys:
    - name: the name of the item to be created
    - group_name: The name of the group where the new item will belong to. group name can be only considered
    for groups that are not subgroups. Either group_name or group_id must be specified
    - group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
    - category_name: the name of the category that the new item will belong to. Either category_name or category_id must be specified
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
  - category_id: the id of the category that the new item will belong to. Either category_name or category_id must be specified

:return list with instance of the experiment class

#### datatables *: `List`[[`DataTable`](#furthrmind_sdk.collection.datatable.DataTable)]* *= []*

#### fielddata *: `List`[[`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)]* *= []*

#### files *: `List`[[`File`](#furthrmind_sdk.collection.file.File)]* *= []*

#### *classmethod* get(id)

Method to get all one researchitem by it’s id or short_id
If called on an instance of the class, the id of the class is used
:param str id: id or short_id of requested researchitem 
:return Self: Instance of researchitem class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all researchitems belonging to one project
:param str project_id: Optionally to get researchitems from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of researchitem class

* **Return type:**
  `List`[`Self`]

#### *classmethod* get_by_name(name, category_name, project_id=None)

#### groups *: `List`[[`Group`](#furthrmind_sdk.collection.group.Group)]* *= []*

#### id *= ''*

#### linked_experiments *: `List`[[`Experiment`](#furthrmind_sdk.collection.experiment.Experiment)]* *= []*

#### linked_researchitems *: `Dict`[`str`, `List`[[`ResearchItem`](#furthrmind_sdk.collection.researchitem.ResearchItem)]]* *= {}*

#### linked_samples *: `List`[[`Sample`](#furthrmind_sdk.collection.sample.Sample)]* *= []*

#### name *= ''*

#### neglect *= False*

#### shortid *= ''*

## furthrmind_sdk.collection.sample module

### *class* furthrmind_sdk.collection.sample.Sample(id=None, data=None)

Bases: [`BaseClassWithFieldData`](#furthrmind_sdk.collection.baseclass.BaseClassWithFieldData), [`BaseClassWithFiles`](#furthrmind_sdk.collection.baseclass.BaseClassWithFiles), [`BaseClassWithGroup`](#furthrmind_sdk.collection.baseclass.BaseClassWithGroup)

#### \_\_init_\_(id=None, data=None)

#### add_datatable(name, columns=None, project_id=None)

Method to create a new datatable within this experiment

* **Parameters:**
  * **name** (`str`) – name of the datatable
  * **columns** (`Optional`[`List`[`Dict`]]) – a list of columns that should be added to the datatable. List with dicts with the following keys:
    - name: name of the column
    - type: Type of the column, Either “Text” or “Numeric”. Data must fit to type, for Text all data
    will be converted to string and for Numeric all data is converted to float (if possible)
    - data: List of column values, must fit to column_type
    - unit: dict with id or name, or name as string, or id as string
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  [`DataTable`](#furthrmind_sdk.collection.datatable.DataTable)
* **Returns:**
  instance of column datatable class

#### *classmethod* create(cls, name, group_name=None, group_id=None, project_id=None)

Method to create a new sample

* **Parameters:**
  * **name** – the name of the item to be created
  * **group_name** – The name of the group where the new item will belong to. group name can be only considered
    for groups that are not subgroups. Either group_name or group_id must be specified
  * **group_id** – the id of the group where the new item will belong to. Either group_name or group_id must be specified
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`

:return instance of the sample class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create multiple samples

* **Parameters:**
  * **data_list** (`List`[`Dict`]) – dict with the following keys:
    - name: the name of the item to be created
    - group_name: The name of the group where the new item will belong to. group name can be only considered
    for groups that are not subgroups. Either group_name or group_id must be specified
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
  - group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified

:return list with instance of the sample class

#### datatables *: `List`[[`DataTable`](#furthrmind_sdk.collection.datatable.DataTable)]* *= []*

#### fielddata *: `List`[[`FieldData`](#furthrmind_sdk.collection.fielddata.FieldData)]* *= []*

#### files *: `List`[[`File`](#furthrmind_sdk.collection.file.File)]* *= []*

#### *classmethod* get(id=None, name=None)

Method to get all one sample by it’s id or short_id
If called on an instance of the class, the id of the class is used
:param str id: id or short_id of requested sample 
:param str name: name of requested sample 
:return Self: Instance of sample class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all samples belonging to one project
:param str project_id: Optionally to get samples from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of sample class

* **Return type:**
  `List`[`Self`]

#### groups *: `List`[[`Group`](#furthrmind_sdk.collection.group.Group)]* *= []*

#### id *= ''*

#### linked_experiments *: `List`[[`Experiment`](#furthrmind_sdk.collection.experiment.Experiment)]* *= []*

#### linked_researchitems *: `Dict`[`str`, `List`[[`ResearchItem`](#furthrmind_sdk.collection.researchitem.ResearchItem)]]* *= {}*

#### linked_samples *: `List`[`Self`]* *= []*

#### name *= ''*

#### neglect *= False*

#### shortid *= ''*

## furthrmind_sdk.collection.unit module

### *class* furthrmind_sdk.collection.unit.Unit(id=None, data=None)

Bases: [`BaseClass`](#furthrmind_sdk.collection.baseclass.BaseClass)

#### \_\_init_\_(id=None, data=None)

#### *classmethod* create(cls, name, definition=None, project_id=None)

Method to create a new unit

* **Parameters:**
  * **name** (`str`) – name of the new unit
  * **definition** (`Optional`[`str`]) – Unit definition in SI units to convert the new unit to an SI Value. E.g. for unit cm², the
    definition would be: ‘cm \* cm’. For valid units please check the webapp, open the unit editor.
    You will find there a list of valid units. A definition can als contain scalar values.
  * **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  instance of the unit class

#### *classmethod* create_many(cls, data_list, project_id=None)

Method to create a new unit

* **Parameters:**
  **data_list** – List of dictionaries with the following keys:

- name: name of the new unit
- definition: Unit definition in SI units to convert the new unit to an SI Value. E.g. for unit cm², the
  : definition would be: ‘cm \* cm’. For valid units please check the webapp, open the unit editor.
    You will find there a list of valid units. A definition can als contain scalar values.

* **Parameters:**
  **project_id** – Optionally to create an item in another project as the furthrmind sdk was initiated with
* **Return type:**
  `Self`
* **Returns:**
  instance of the unit class

#### definition *= ''*

#### *classmethod* get(id=None)

Method to get all one unit by it’s id
If called on an instance of the class, the id of the class is used
:param str id: id of requested category 
:return Self: Instance of unit class

* **Return type:**
  `Self`

#### *classmethod* get_all(project_id=None)

Method to get all units belonging to one project
:param str project_id: Optionally to get units from another project as the furthrmind sdk was initiated with, defaults to None
:return List[Self]: List with instances of unit class

* **Return type:**
  `List`[`Self`]

#### id *= ''*

#### longname *= ''*

#### name *= ''*

## Module contents

### furthrmind_sdk.collection.get_collection_class(collection_name)
