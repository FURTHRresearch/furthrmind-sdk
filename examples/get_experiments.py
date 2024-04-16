from furthrmind.furthrmind import FURTHRmind
from furthrmind.collection import Experiment
import os
 
home_path = os.path.expanduser("~")
api_key_path = os.path.join(home_path, "furthrmind_demo_api_key") 


fm = FURTHRmind(host="http://127.0.0.1:5000", api_key_file=api_key_path, project_name="Maskentests_1")


# get specific experiment:

# by short-id which can be copied from the webapp
exp = Experiment.get("exp-c2ills")    
print(exp.id)
print(exp.name)

exp = exp.get()

# by id
exp = Experiment.get("6319f80801c844a436e175ee")    

# by name 
exp = Experiment.get(name="3M - 9501V+_LH326_P_Maskentest")

# To iterate all fields attached to an item, just take the fielddata attribute and iterate it. Each
# item in this list will be an fielddata object.
for fielddata in exp.fielddata:
    print(f"{fielddata.field_name}: {fielddata.value}, field type: {fielddata.field_type}")


# get attached items
for sample in exp.linked_samples:
    print(f"Sample: {sample.name}")
    # linked items are not complete when requested, that means that fielddata, datatables, file, etc are still missing. E.g. Fielddata list is empty
    print("Fielddata:", len(sample.fielddata))
    # In order to request these data, call the get method on the instance of this object
    sample = sample.get()
    # Now, all information are requested.
    print("Fielddata:", len(sample.fielddata))

# get attached researchitems. Researchitems are not stored in a list, but in a dictionay with the category name as it's keys. 
for cat in exp.linked_researchitems:
    print(f"Category: {cat}")
    for researchitem in exp.linked_researchitems[cat]:
            print(f"ResearchItem: {researchitem.name}")

# get attached items
for linked_exp in exp.linked_experiments:
    print(f"Exp: {linked_exp.name}")


