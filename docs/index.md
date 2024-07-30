# FURTHRmind python package

This package provides a simple and user-friendly way to interact with your FURTHRmind application. It enables users to
effortlessly retrieve existing data or write new data into the application.

## Install

You can conveniently install `furthrmind` from PyPi using the following command:
```
pip install furthrmind
```

## Basic usage

### Retrieve objects

To initiate an interaction with your server through the Furthrmind class, you need to create an instance of it. You will
pass in your server's URL and API key. Don’t forget to provide the name or ID of the project you want to work with.

```
from furthrmind import Furthrmind
fm = FURTHRmind(host, api_key, project_name="my project")
```

Retrieving data necessitates the importation of the relevant collection class. This can be attained either from your
Furthrmind instance or by direct import.

```
Experiment = fm.Experiment
from furthrmind.collection import Experiment
```

To fetch a specific experiment, invoke the get method of the Experiment class, passing in the desired experiment's ID.

```
exp = fm.Experiment.get(exp_id)
```

or

```
exp = Experiment.get(exp_id)
```

Both these commands are identical provided the Experiment class was previously imported.

You can fetch all the experiments from a project by calling the get_all method which returns a list of instances of the
Experiment class.

```
exp_list = Experiment.get_all()
```

The Experiment class instance encapsulates all data pertinent to your experiment. For convenience, this class provides
several methods including: add_field, add_many_fields, remove_field, update_field_value, update_field_unit, add_file,
remove_file, and add_datatable. Details about the available methods for each collection class can be found below.

### Nested objects

In the preceding example, we retrieved one or more experiments from the Furthrmind server. Each experiment encompasses
various attributes such as the corresponding samples, research items, and the group to which it belongs. Note that these
entities are nested objects.

For instance, the 'groups' attribute comprises a list of group instances belonging to the group collection class. To
optimize network traffic, these nested objects do not load completely. In other words, all properties, except for the '
id' and 'name', remain unretrieved.

To verify whether an object has been fully loaded, you can inspect the `_fetched` attribute of the object. If an object
hasn't been fetched yet, you can invoke the `get()` method on that object to retrieve it.

### Create new objects

To generate a new experiment, you should invoke the `create()` or `create_many()` method. It's important to correctly
supply the input arguments suitable for each collection class. Specifically, the `create` method of the `Experiment`
class necessitates passing the new experiment's name, and the name or ID of the group to which it should belong.

In case your requirement entails adding an experiment to a subgroup, supplying this subgroup's ID becomes paramount.
The `create` method subsequently gives back an instance of the `Experiment` class, whereas the `create_many` method
yields a list of `Experiment` class instances.

```
new_exp = Experiment.create("myexperiment2", group_name="My group"
```

Alternatively, to create multiple experiments:

```
experiments = Experiment.create_many([{"name": "exp1", "group": "group1"}, {"name": "exp2", "group": "group2"}])

```

### Adding fields, files, and datatables

After you created the new experiment you might want to add some fields, files, and datatables to your
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

## A list of collections and its method to work with can be found here:
[experiment](experiment.md)

Get a project
pass the id or name of the project you want to retrieve

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