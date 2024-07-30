# Project

## Attributes

Projects do have the following attributes:

- `id`: id of the project
- `name`: name of the project
- `info`: Detailed information belonging to the project
- `shortid`: shortid of the project
- `groups`: This is a list of all groups related to this project. Each entry is a partially fetched `group` object,
  containing just the name and id. More details on this can be found in the section
  on [nested objects](../README.md#nested-objects).
- `samples`: This is a list of all samples associated with this project. Each entry is a partially fetched `sample`
  object, containing just the name and id. More details on this can be found in the section
  on [nested objects](../README.md#nested-objects).
- `experiments`: This is a list of all experiments linked to this project. Each entry is a partially
  fetched `experiment` object, containing just the name and id. More details on this can be found in the section
  on [nested objects](../README.md#nested-objects).
- `resarchitems`: This is a dictionary with category name as keys and lists and the corresponding researchitem objects as values. 
  Each list entry is a partially fetched `researchitem` object, containing just the name and id. 
  More details on this can be found in the section on [nested objects](../README.md#nested-objects). 
- `fields`: This is a list of all fields associated with this project. Each item in the list is a completely fetched `field` object.
- `units`: This is a list of all units belonging to this project. Each item in the list is a completely fetched `unit` object
- `permissions`: This is a dictionary with the following keys: `owner`: the owner of the project, `users`: List of 
  users having access to this project including their access level, `user`


## Methods

#### get(id="", name="")