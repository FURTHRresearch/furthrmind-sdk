from furthrmind_sdk.furthrmind import FURTHRmind
from furthrmind_sdk.collection import Experiment, Group
import os
 
home_path = os.path.expanduser("~")
api_key_path = os.path.join(home_path, "furthrmind_demo_api_key") 


fm = FURTHRmind(host="http://127.0.0.1:5000", api_key_file=api_key_path, project_name="test")

# in order to create a group, you can call:
group = Group.create(name="My new group")

# in order to create many new groups in once, you can call
name_list = ["My new group 2", "My new group 3"]
groups = Group.create_many(name_list)

group = groups[0]
print(group.id)

# If you want to add fields to your group:
group.add_field("My numeric field", "Numeric", value=5, unit="cm")


# in order to create a new experiment:
exp = Experiment.create(name="My exp", group_id=group.id)

# in order to create many experiments:
experiments = [
    {"name": "My exp 2",
     "group_id": group.id},
    {"name": "My exp 3",
     "group_id": group.id},
]
exp_list = Experiment.create_many(experiments)

print(exp_list)