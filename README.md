# furthrmind-sdk

This package allows to easily interact with your FURTHRmind application in order to retrieve data or to write new
data.

## Install
```
pip install furthrmind-sdk
```

## Basic usage

Create an instance of the furthrmind class and pass the url to your server, your api key. 
Optionally you can pass the project name or id of the project you would like to work with.

```
from furthrmind_sdk.furthrmind import FURTHRmind
fm = FURTHRmind(host, api_key, project_name="my project")
```

In order to retrieve data, you have to import the corresponding collection class and call the
get or get_all method. The method will return an instance / a list with instances of the 
Experiment class. The instance of the experiment class will contain all data that belong to
your experiment. Additionally, the experiment object has some convenient method for:
add_field, add_many_fields, remove_field, update_field_value, update_field_unit, add_file, 
remove_file, add_datatable

```
furthrmind_sdk.collection import Experiment
exp_list = Experiment.get_all()
```

To create a new experiment, you need to call the create() or create_many() method. Please 
consider the correct input arguments for each collection class. For experiments, the create
method expects to pass the new exp name and the name or id of the group that it should belong to. 
If you want to add an experiment to a subgroup, you need to pass the id of this group. The 
create method will return an instance of the Experiment class, the create_many method will
return a list with instances of the Experiment class

```
new_exp = Experiment.create("myexperiment2", group_name="My group"
```

After you created the new you might want to add some fields, files, and datatables to your
experiment. This can be achieved with:

```
new_exp.add_field(field_name="My field namy", field_type="Numeric",
                  value=5, unit="cm")
new_exp.add_many_fields([
        {
            "name": "May field name,
            "field_type" ="Numeric",
            "value: 5, 
            "unit": "cm"
        },
        {
            "name": "May second field name,
            "field_type" ="Numeric",
            "value: 10, 
            "unit": "m"
        }
])
new_exp.add_file(my_file_path)
new_exp.add_datatable(name=my data table, columns=[
        {
            "name": "my 1st column"
            "type": "Numeric,
            "unit": "cm",
            "data": [1,2,3]
        },
        {
            "name": "my 2nd column"
            "type": "Numeric,
            "unit": "cm",
            "data": [4,5,6]
        },
])
```

### A list of collections to work with can be found here:
- Project 
- Group
- Experiment
- Sample
- ResearchItem
- Field
- FieldData (the fields attached to an item: experiments, samples, or researchitems)
- Unit
- File 
- DataTable
- Column
- ComboBoxEntry (the entries within a list field)
- Category 